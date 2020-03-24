#coding:utf-8
#VS写的第一个Python程序
import tkinter.messagebox 
#tkinter.messagebox.askokcancel('提示','答对了亲')
if __name__=="__main__":
    sum1 = input("1+1等于几?\n")
    if(sum1=="2"):
        tkinter.messagebox.askokcancel('提示','答对了亲')
        input("答对了亲，回车退出程序吧")
    else:
        input("答错了亲，请按回车键结束")   

    