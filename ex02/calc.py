import tkinter as tk
import tkinter.messagebox as tkm

# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        res = eval(entry.get())
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入

    elif num == "00": #00を入力したときに0にされないようにしたかった
        entry.insert(tk.END, "0")
        entry.insert(tk.END, "0")

    elif num == "×": #掛け算
        entry.insert(tk.END, "*")

    elif num == "÷": #割り算
        entry.insert(tk.END, "/")

    elif num == "C": #reset
        entry.delete(0, tk.END)
        
    else: # 「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

#クリックしたときエントリ内を削除
def reset_button_click(event):
    # btn = event.widget
    entry.delete(0, tk.END)

    
# 練習１
root = tk.Tk()
root.geometry("400x700") #4列を表示できる横幅

# 練習４
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)

# 練習２
r, c = 1, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

#ボタン追加機能（演算に使えるモノのみ）
add_num = [00, "."]
for num in add_num:
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0


#リセットボタンC
reset_button = tk.Button(root, text="C", width=4, height=2, font=("", 30), bg="#fff")
reset_button.grid(row=r, column=0)
reset_button.bind("<1>", button_click)


# 練習５
operators = ["+", "-", "×", "÷", "="]
r = 1 #高さをリセット
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30), bg="DeepSkyBlue4")
    button.grid(row=r, column=4) #数字の右側に演算子を配置
    button.bind("<1>", button_click) 
    r += 1
    # if c%3 == 0:
    #     r += 1
    #     c = 0



root.mainloop()
