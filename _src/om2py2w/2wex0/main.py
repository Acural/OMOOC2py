# -*- coding:utf-8 -*-
from Tkinter import *
from os.path import exists
import time   #调用时间函数.

root = Tk()
root.title("我的日记")
root.geometry('800x600')

txt = "mydaily.txt"

# 历史记录&退出功能使用menu模块得以实现
def history():
    if exists(txt):
        daily = open(txt,'r')
        T.insert(END,"历史记录：\n")
        T.insert(END,daily.read())
        txt.close()
    else:  
        T.insert(END,"无历史记录，开始记录吧")

T = Text(root,height = 15, font = "Arial 14")
T.pack()

# 日记书写程序
def write():
    
    target = open(txt,'a')

    
    now = time.strftime ("%Y-%m-%d %H:%M:%S")  #写作时的时间           
    target.write("creatime:")
    target.write(now)
    target.write("\n")

    #line = E.get().encode("utf-8") #why why why ????
    #target.write(line)
    s = w.get().encode("utf-8")  #实现中文输入
    target.write(s)
    target.write("\n")
    target.write("\n")                    
    
    target.close()
    w.delete(0, END)
    
    #把书写内容添加到屏幕
    target.insert(END, s)

#书写界面的调试
frm = Frame(root,height=10)   #设置frame框架
frm.pack()

l=Label(frm, text="请输入您的日记 按input保存") #提示框
l.pack(side=LEFT)

w=Entry(frm, width=80)
w.pack()

# 书写界面输入按钮  未实现
#button = Button(frm,text="input",fg="red", commmand = write)
#button.pack(side = right,padx = 5, pady = 2)

menubar = Menu(root)
menubar.add_command(label="History",command=history)
  
menubar.add_command(label="Input",command=write)

menubar.add_command(label="Quit",command=root.quit) 
root.config(menu=menubar)



root.mainloop()

