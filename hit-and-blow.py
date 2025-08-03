import random

# 0-9までのランダムな数字を決める
answer = random.randint(0, 9)

while True:
    try:
        #ユーザに0－9の数字を入力してもらう
        user_input_str = input("0-9の数字を入力してください: ")
        # 入力が空の場合は再度入力を促す
        if not user_input_str:
            continue
        user_input = int(user_input_str)

        #数字が0－9でない場合は、エラーメッセージを表示する
        if user_input < 0 or user_input > 9:
            print("0-9の数字を入力してください")
            continue

        #answerとuser_inputの数字が一致している場合は、hitを表示する
        if answer == user_input:
            print("hit! 正解です！")
            break
        else:
            print("blow")

    except ValueError:
        print("有効な数字を入力してください。")
