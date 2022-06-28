import tkinter as tk
from tkinter import Canvas
import maze_maker as mm
import tkinter.messagebox as tkm



def key_down(event):
    global key, num,tori,cx,cy
    key = event.keysym
    if key == "r":
        num += 1
        canvas.delete(kya)
        tori = tk.PhotoImage(file=f"ex03/fig/{str(num)}.png")
        canvas.create_image(cx, cy, image= tori, tag= "tori")
        if num > 9:
            num = 0
    if key == "k":
        cx = 1300
        cy = 750

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, 

    delta = { #キー：押されているキーkey/値:移動幅リスト[x,y]
        ""  :[0,0],
        "Up":[0,-1],
        "Down":[0,+1],
        "Left":[-1,0],
        "Right":[+1,0],

    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 1:
            pass
        else:
            mx, my = mx+delta[key][0], my+delta[key][1]
            cx, cy = mx*100+50, my*100+50
    except:
        pass
    canvas.coords("tori", cx, cy)
    if cx == 1350 and cy == 750:
        tkm.showinfo("こうかとん", "Game Clear")
        return False
    root.after(100, main_proc)
if __name__ == "__main__":
    num = 0

    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas, maze_bg)

    tori = tk.PhotoImage(file=f"ex03/fig/{str(num)}.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_rectangle(cx-50, cy-50, cx+50, cy+50, fill="blue")
    canvas.create_rectangle(1300, 700, 1400, 800, fill="red")
    
    kya = canvas.create_image(cx, cy, image= tori, tag= "tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()
