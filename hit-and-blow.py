import random
import tkinter as tk
from tkinter import messagebox

class HitAndBlowGame:
    def __init__(self, master):
        self.master = master
        master.title("Hit & Blow")
        master.geometry("400x400") # ウィンドウサイズを指定

        # --- ゲームの内部的な準備 ---
        # 正解の数字を生成
        self.answer = random.sample(range(10), 4)
        # チャレンジ回数
        self.attempts = 0
        # デバッグ用に答えをコンソールに表示したい場合は下のコメントを外す
        print(f"正解は: {''.join(map(str, self.answer))}")

        # --- GUIウィジェットの作成と配置 ---
        self.info_label = tk.Label(master, text="4桁の数字を入力してください", font=("Helvetica", 12))
        self.info_label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 14), justify='center')
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(master, text="予想する", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(master, text="結果:", font=("Helvetica", 12))
        self.result_label.pack(pady=5)

        # 履歴を表示するリストボックス
        self.history_listbox = tk.Listbox(master, height=10, font=("Courier", 12))
        self.history_listbox.pack(pady=10, padx=20, fill="both", expand=True)

    def check_guess(self):
        user_input_str = self.entry.get()

        # --- 入力値のバリデーション ---
        if not user_input_str.isdigit() or len(user_input_str) != 4:
            messagebox.showerror("入力エラー", "4桁の数字を入力してください。")
            self.entry.delete(0, tk.END)
            return
        
        # 重複チェック
        if len(set(user_input_str)) != 4:
            messagebox.showerror("入力エラー", "数字は重複しないように入力してください。")
            self.entry.delete(0, tk.END)
            return

        user_input = [int(digit) for digit in user_input_str]

        # --- HitとBlowの計算 ---
        hit = 0
        blow = 0
        for i in range(4):
            if user_input[i] == self.answer[i]:
                hit += 1
            elif user_input[i] in self.answer:
                blow += 1
        
        self.attempts += 1
        result_text = f"Hit: {hit}, Blow: {blow}"
        self.result_label.config(text=result_text)

        # 履歴に追加
        history_entry = f"{self.attempts:2d}: {user_input_str} -> {result_text}"
        self.history_listbox.insert(tk.END, history_entry)
        self.history_listbox.see(tk.END) # 常に最新の履歴が見えるようにスクロール

        # --- 正解判定 ---
        if hit == 4:
            self.result_label.config(text=f"正解です！ ({self.attempts}回でクリア)")
            self.entry.config(state='disabled')
            self.guess_button.config(state='disabled')
            messagebox.showinfo("おめでとう！", f"正解です！\n正解の数字は「{''.join(map(str, self.answer))}」でした。")

        # 入力ボックスをクリア
        self.entry.delete(0, tk.END)

# --- アプリケーションの実行 ---
if __name__ == "__main__":
    root = tk.Tk()
    game = HitAndBlowGame(root)
    root.mainloop()
