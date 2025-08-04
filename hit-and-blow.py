import random

# 0から9までの数字から、重複を許して4回選ぶ
answer = random.sample(range(0, 10), k=4)
# 数字を0埋め4桁の文字列にする場合は、このようにできます
answer_str = "".join(map(str, answer))
print(f"生成された文字列: {answer_str}")

while True:
        #ユーザに４桁の数字を入力してもらう
        user_input_str = input("４桁の数字を入力してください: ")
        # 入力が空の場合は再度入力を促す
        if not user_input_str:
            print("４桁の数字を入力してください")
            continue
        # 4桁であるかをチェックする
        if len(user_input_str) != 4:
            print("４桁の数字を入力してください")
            continue
        # 4桁をそれぞれ1桁ずつに分割してリストにする
        user_input = [int(digit) for digit in user_input_str]
        # 入力リストと回答文字列を比較する
        hit = 0
        blow = 0
        # リスト同士の要素番号一致で同じ値だったらヒットでカウントアップする
        # ヒットしていない場合、リストの異なる要素番号に同じ値が入ったらブローとしてカウントアップする
        for i in range(4):
            if user_input[i] == answer[i]:
                hit += 1
            elif user_input[i] in answer:
                blow += 1  
        # 最後にヒットとブロー数を表示する
        print(f"ヒット: {hit}, ブロー: {blow}")
       # 4件ヒットしてたら正解と表示して終了する
        if hit == 4:
            print("正解です！")
            break 
