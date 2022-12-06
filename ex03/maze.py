import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc(tag_inf): #引数でタグ情報を入手
    global cx, cy, mx, my
    kouka_form = "" #キー入力で得られるタグの情報を保持する変数
    if key == "Up": 
        my -= 1
        kouka_form = up_koukaton #キーが上の時の場合のタグ情報を保持
  
    if key == "Down":
        my += 1
        kouka_form = dw_koukaton

    if key == "Left": 
        mx -= 1
        kouka_form = le_koukaton
    
    if key == "Right": 
        mx += 1
        kouka_form = ri_koukaton
       
    if key:
        canvas.delete(f"{tag_inf}") #タグ指定し、移動前のこうかとんを削除
    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx,cy = mx*100+50, my*100+50
    
    canvas.create_image(cx, cy, image=kouka_form, tag=f"{kouka_form}") #こうかとん画像を作成
    root.after(100, main_proc, kouka_form)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="red2")


    #こうかとんフォルムチェンジ用imegeオブジェクト作成
    de_koukaton = tk.PhotoImage(file="fig/1.png") #デフォルトのこうかとん
    up_koukaton = tk.PhotoImage(file="fig/6.png") #上向きのこうかとん
    dw_koukaton = tk.PhotoImage(file="fig/8.png") #下のこうかとん
    le_koukaton = tk.PhotoImage(file="fig/3.png") #左のこうかとん
    ri_koukaton = tk.PhotoImage(file="fig/2.png") #右のこうかとん


    mx,my = 1,1
    cx,cy = mx*100+50, my*100+50
    
    
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)
    canvas.create_image(cx, cy, image=de_koukaton, tag="koukaton")
    canvas.pack()
    
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc(de_koukaton)
    root.mainloop()
