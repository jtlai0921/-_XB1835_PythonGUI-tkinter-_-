# ch9_10.py
from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())

def Delete():
    sp.delete(0)
    
root = Tk()
root.title("ch9_9")
cities = ["新加坡","上海","東京"]       # 以元組儲存數值

sp = Spinbox(root,
             values=cities,    
             command=printInfo)
sp.pack(pady=10,padx=10)

btn = Button(root,text="Delete",command=Delete)
btn.pack(pady=10)

root.mainloop()






