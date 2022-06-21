import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo(num, f"[{num}のボタンが押されました]")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("300x500")
    
    r, c = 0,0      #    r:行番号　c:列番号

    for num in range(9,-1,-1):
        btn = tk.Button(root, text=f"{num}", width=4,height=2,font=("Times New Roman", 30))
        btn.bind("<1>", button_click)
        btn.grid(row=r,column=c)
        c += 1
        if (num-1)%3 == 0:
            r += 1
            c = 0






    root.mainloop()
    