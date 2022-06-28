import tkinter as tk
from tkinter import Canvas as cav

def key_down(event):
    global key
    key = event.keysym
    print(key)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    tori = tk.PhotoImage(file="ex03/fig/5.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image= tori, tag= tori)

    key = ""
    root.bind("<KeyPress>", key_down)

    root.mainloop()