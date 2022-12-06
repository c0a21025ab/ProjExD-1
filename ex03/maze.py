import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx,cy = mx*100+50, my*100+50
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    koukaton = tk.PhotoImage(file="fig/8.png")
    mx,my = 1,1
    cx,cy = mx*100+50, my*100+50
    
    
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
    canvas.pack()
    
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
