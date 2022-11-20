from tkinter import *


root=Tk()


root.title('Simple Calculator')

e=Entry(root,width=50, borderwidth=5)
e.grid(row=0,column=0,columnspan=4)



def onclick(n):
    
    num=e.get()
    e.delete(0,END)
    e.insert(0,str(num)+n)


def clear():
    e.delete(0,END)
    
    
def add():
    global n1
    n1=e.get()
    n1=int(n1)
    global math
    math='Addition'
    e.delete(0,END)


def diff():
    global n1
    n1=e.get()

    n1=int(n1)
    global math
    math='Subtract'
    e.delete(0,END)
    
   
def prod():
    global n1
    n1=e.get()
    n1=int(n1)
    global math
    math='Multiply'
    e.delete(0,END)
    
    
def div():
    global n1
    n1=e.get()
    n1=int(n1)
    global math
    math='Division'
    e.delete(0,END)


def mod():
    global n1
    n1=e.get()
    n1=int(n1)
    global math
    math='Div'
    e.delete(0,END)
    
   
def square():
    num=int(e.get())
    e.delete(0,END)
    e.insert(0,num*num)


def mr():
    global num
    num=e.get()
    num=int(num)
    e.delete(0,END)

def mc():
    e.insert(0,num)
    

    
def equals():
    n2=e.get()
    e.delete(0,END)
    n2=int(n2)

    if math=='Addition':
        e.insert(0,(n1+n2))

    elif math=='Subtract':
        e.insert(0,(n1-n2))

    elif math=='Multiply':
        e.insert(0,(n1*n2))

    elif math=='Division':
        if n2==0:
            e.insert(0,'Error')

        else:
            e.insert(0,(n1/n2))
        
    elif math=='Div':
        if n2==0:
            e.insert(0,'Error')

        else:
            e.insert(0,(n1%n2))
       
    
    
    


b1=Button(root,text='1',padx=40,pady=20,command=lambda:onclick('1'))
b2=Button(root,text='2',padx=40,pady=20,command=lambda:onclick('2'))
b3=Button(root,text='3',padx=40,pady=20,command=lambda:onclick('3'))
b4=Button(root,text='4',padx=40,pady=20,command=lambda:onclick('4'))
b5=Button(root,text='5',padx=40,pady=20,command=lambda:onclick('5'))
b6=Button(root,text='6',padx=40,pady=20,command=lambda:onclick('6'))
b7=Button(root,text='7',padx=40,pady=20,command=lambda:onclick('7'))
b8=Button(root,text='8',padx=40,pady=20,command=lambda:onclick('8'))
b9=Button(root,text='9',padx=40,pady=20,command=lambda:onclick('9'))
b0=Button(root,text='0',padx=40,pady=20,command=lambda:onclick('0'))

bmc=Button(root,text='MC',padx=33,pady=20,command=mc)
bplus=Button(root,text='+',padx=39,pady=20,command=add)
bdiff=Button(root,text='-',padx=39,pady=20,command=diff)
bprod=Button(root,text='*',padx=39,pady=20,command=prod)
bdiv=Button(root,text='/',padx=39,pady=20,command=div)
bmod=Button(root,text='%',padx=39,pady=20,command=mod)
bmr=Button(root,text='MR',padx=34,pady=20,command=mr)
bsq=Button(root,text='X^2',padx=33,pady=20,command=square)

bequals=Button(root,text='=',padx=39,pady=20,command=equals)
bclear=Button(root,text='Clear',padx=30,pady=20,command=clear)






b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)
b0.grid(row=5,column=2)

bmc.grid(row=1,column=1)


print(type(b1))

bplus.grid(row=4,column=3)
bdiff.grid(row=3,column=3)
bprod.grid(row=2,column=3)
bdiv.grid(row=1,column=3)
bmod.grid(row=5,column=0)
bmr.grid(row=1,column=2)
bsq.grid(row=5,column=1)


bclear.grid(row=1,column=0,columnspan=1)
bequals.grid(row=5,column=3,columnspan=1)
root.mainloop()
