import random
from pathlib import Path
from tkinter import *

def randomly_split(original_number):
    r= random.randint(1, original_number)
    l= original_number - r
    
    return r, l


def one_change():
    a1=49
    l1,r1=randomly_split(a1)
    r1=(r1-1)%4
    l1=l1%4
    e1=0
    if r1==0:
        if l1==0:
            e1=9
        else:
            e1=5
    else:
        e1=5

    a2=a1-e1
    r2,l2=randomly_split(a2)
    r2=(r2-1)%4
    l2=l2%4
    e2=0
    if r2==0:
        e2=8
    elif l2==0:
        e2=8
    else:
        e2=4

    a3=a2-e2
    r3,l3=randomly_split(a3)
    r3=(r3-1)%4
    l3=l3%4
    e3=0
    if r3==0:
        e3=8
    elif l3==0:
        e3=8
    else:
        e3=4
    
    e=e1+e2+e3
    ans=0

    if e==21 or e==22:
        ans='--------- '
    elif e==17 or e==18:
        ans='---   --- '
    elif e==13 or e==14:
        ans='---------'
    elif e==25 or e==26:
        ans='---   ---'

    return ans

def show():
    c1=one_change()   #chatgpt:return tuple(one_change() for _ in range(6))
    c2=one_change()  
    c3=one_change()  
    c4=one_change()  
    c5=one_change()  
    c6=one_change()     
    return c1, c2, c3, c4, c5, c6


def result():
    global tk2
    tk2 = Toplevel(tk)
    tk2.title("算卦結果")
    tk2.geometry('200x350+50+70')

    c1,c2,c3,c4,c5,c6=show()
    lbl1=Label(tk2, text=c1, font=('arial',40))
    lbl2=Label(tk2, text=c2, font=('arial',40))
    lbl3=Label(tk2, text=c3, font=('arial',40))
    lbl4=Label(tk2, text=c4, font=('arial',40))
    lbl5=Label(tk2, text=c5, font=('arial',40))
    lbl6=Label(tk2, text=c6, font=('arial',40))

    lbl1.grid(row=1, column=0)
    lbl2.grid(row=2, column=0)
    lbl3.grid(row=3, column=0)
    lbl4.grid(row=4, column=0)
    lbl5.grid(row=5, column=0)
    lbl6.grid(row=6, column=0)

    btn2 = Button(tk2, text='查看詳細內容', width=15, command=result2)
    btn2.grid(row=7, column=0)

def result2():
    global tk3
    tk3=Toplevel(tk2)
    tk3.title('總覽')

    global enyl
    enyl=Entry(tk3)
    enyl.insert(1,'請輸入圖案對應的名稱')
    btn3 = Button(tk3, text='查看解析', command=result3)
    btn3.grid(row=1, column=0)

    gra=PhotoImage(file='content2.png')
    lbl0=Label(tk3, image=gra)
    enyl.grid(row=0, column=0)
    lbl0.grid(row=2, column=0)
    tk3.mainloop()

def result3():
    tk4 = Toplevel(tk3)
    tk4.title('解析')
    user_input = enyl.get()
    file_path = Path(user_input + '.txt')

    if file_path.exists():
        lblt = Label(tk4, text=file_path.read_text())
        lblt.pack()
        print(file_path.read_text())
    else:
        lblt = Label(tk4, text='請確認是否輸入錯誤')
        lblt.pack()

    tk4.mainloop()


tk = Tk()
tk.title('易經卜卦')
lbl1=Label(tk, text='在心中默想問題，再按下算卦')
btn1 = Button(tk, text='算卦', width=30, command=result)
btn1.grid(row=0, column=0)
lbl1.grid(row=1, column=0)
tk.mainloop()








