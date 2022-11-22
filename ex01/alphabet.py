import random
import string
import time

num_of_alphabet = 26
taiou = 10
kesson = 2
kaisuu = 2
def shutudai(alpha):
    taishou = random.sample(alpha, taiou)
    taishou_2 ="" 
    
    print("対象文字：")
    for m in taishou:
        print(m, end=" ")


    abs_mozi = random.sample(taishou, kesson)
   
    
    print("表示文字：")
    for m in taishou:
        if m not in abs_mozi:
            print(m, end=" ")
    print()

    return abs_mozi


    
def kaitou(abs_mozi):
    num = int(input("欠損文字はいくつあるでしょうか： "))
    if num != kesson:
        print("不正解です。")
        

    else:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください：")

    for i in range(num):
        ans = input(f"{i + 1}つ目の文字を入力してください：")
        if ans not in abs_mozi:
            print("不正解です")
            return False
        else:
            abs_mozi.remove(ans)

    print("全部正解です。")
    return True







if __name__ == "__main__":
    st = time.time()
    alpha = list(string.ascii_uppercase)
    while True:
        kaisuu += 1
        abs_mozi = shutudai(alpha)
        ret = kaitou(abs_mozi)
        if ret:
            break
        else:
            print("-"*20)

    ed = time.time()
    print(f"所要時間：{(ed-st):.2f}秒")
        

    