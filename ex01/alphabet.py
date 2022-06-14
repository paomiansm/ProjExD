import random
import datetime

NNUM_OF_TRIALS = 5     #最大繰り返し回数
NUM_OF_ALL_CHARS = 10  #対象文字
NUM_OF_ABS_CHARS = 2   #欠損文字

def main():
    st = datetime.datetime.now()  
    for _ in range(NNUM_OF_TRIALS):
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1:
            break
    ed = datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかりました")

def shutudai():
    #全アルファベットの文字リスト
    all_char_lst = random.sample([chr(c+65) for c in range(26)],NUM_OF_ALL_CHARS)
    #26文字からランダムにNUM_OF?ALL_CHARSを取り除く
    print(f"対象文字:{all_char_lst}")

    #対象文字からNUM_OF_ABS_CHARS個の文字をランダムに選ぶ⇒欠損文字
    abs_char_list = random.sample(all_char_lst,NUM_OF_ABS_CHARS)

    print(f"欠損文字:{abs_char_list}")
    #対象文字から欠損文字を除いたもの⇒表示文字
    pre_char_list = []

    print(f"表示文字:{list(set(all_char_lst)-set(abs_char_list))}")
    return abs_char_list

def kaitou(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？："))
    if num != NUM_OF_ABS_CHARS:
        print("不正解です")
        return 0
    else: 
        print("正解です。それでは、具体的に欠損文字を1文字ずつ入力してください")
        for i in range(NUM_OF_ABS_CHARS):
            c = input(f"{i+1}っ目の文字を入力してください：")
            if c not in seika:
                print("不正解です。またチャレンジしてください")
                print("-"*50)
                return 0 #文字解答で不正解
            seikai.remove(c)
        print("全問正解です.")
        return 1 #完全数の場合



if __name__ == "__main__":
    main()


