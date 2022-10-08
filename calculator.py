from tkinter import *
page=Tk()
page.title("Calculator Program")

Frame=LabelFrame(page,padx=0,pady=0,bg="black")
Frame.grid(padx=1,pady=1)

sign_Frame=LabelFrame(page,padx=2,pady=2,bg="black")
sign_Frame.grid(padx=0,pady=0)

#number_Frame=LabelFrame(page,padx=2,pady=2,bg="black")
#number_Frame.grid(padx=0,pady=0)

e=Entry(Frame,width=37,borderwidth=5,bd=5)
e.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

def call(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def clear():
    e.delete(0,END)

def back_delete():
    current=e.get()
    length=len(current)-1
    e.delete(length,END)

def plus():
    first_number=e.get()
    global f_number
    global sign
    sign="+"
    f_number=float(first_number)
    e.delete(0,END)
    
def minus():
    first_number=e.get()
    global f_number
    global sign
    sign="-"
    f_number=float(first_number)
    e.delete(0,END)

def zarb():
    first_number=e.get()
    global f_number
    global sign
    sign="*"
    f_number=float(first_number)
    e.delete(0,END)

def taghsim():
    first_number=e.get()
    global f_number
    global sign
    sign="÷"
    f_number=float(first_number)
    e.delete(0,END)
    
def tavan():
    first_number=e.get()
    global f_number
    global sign
    sign="^"
    f_number=float(first_number)
    e.delete(0,END)

def dot():
    current=e.get()
    if current.find(".")== -1:
        e.delete(0,END)
        e.insert(0,current+".")
    
def equal():
    second=e.get()
    e.delete(0,END)
    if sign=="+":
        e.insert(0,f_number+float(second))
    if sign=="-":
        e.insert(0,f_number-float(second))
    if sign=="*":
        e.insert(0,f_number*float(second))
    if sign=="÷":
        e.insert(0,f_number/float(second))
    if sign=="^":
        e.insert(0,f_number**float(second))
      
#########################################################################################
    
butdarsad=Button(sign_Frame,text="%",padx=15,pady=15,bd=8,bg="pink",fg="black").grid(row=1,column=0)
buttaghsim=Button(sign_Frame,text="÷",padx=15,pady=15,bd=8,bg="pink",fg="black",command=taghsim).grid(row=1,column=1)
butTavan=Button(sign_Frame,text="^",padx=15,pady=15,bd=8,bg="pink",fg="black",command=tavan).grid(row=1,column=2)
butclear=Button(sign_Frame,text="C",padx=15,pady=15,bd=8,fg="black",bg="purple",command=clear).grid(row=1,column=3)

#########################################################################################

but7=Button(sign_Frame,text="7",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(7)).grid(row=2,column=0)
but8=Button(sign_Frame,text="8",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(8)).grid(row=2,column=1)
but9=Button(sign_Frame,text="9",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(9)).grid(row=2,column=2)
butzarb=Button(sign_Frame,text="*",padx=15,pady=15,bd=8,bg="pink",fg="black",command=zarb).grid(row=2,column=3)

#########################################################################################

but4=Button(sign_Frame,text="4",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(4)).grid(row=3,column=0)
but5=Button(sign_Frame,text="5",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(5)).grid(row=3,column=1)
but6=Button(sign_Frame,text="6",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(6)).grid(row=3,column=2)
butminus=Button(sign_Frame,text="_",padx=15,pady=15,bd=8,bg="pink",fg="black",command=minus).grid(row=3,column=3)

#########################################################################################

but1=Button(sign_Frame,text="1",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(1)).grid(row=4,column=0)
but2=Button(sign_Frame,text="2",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(2)).grid(row=4,column=1)
but3=Button(sign_Frame,text="3",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(3)).grid(row=4,column=2)
butplus=Button(sign_Frame,text="+",padx=15,pady=15,bd=8,bg="pink",fg="black",command=plus).grid(row=4,column=3)

#########################################################################################

butback_delete=Button(sign_Frame,text="<×",padx=12,pady=15,bd=8,bg="purple",fg="black",command=back_delete).grid(row=5,column=0)
but0=Button(sign_Frame,text="0",padx=15,pady=15,bd=8,fg="pink",bg="black",command=lambda : call(0)).grid(row=5,column=1)
butdot=Button(sign_Frame,text=".",padx=15,pady=15,bd=8,bg="pink",fg="black",command=dot).grid(row=5,column=2)
butmosavi=Button(sign_Frame,text="=",padx=15,pady=15,bd=8,bg="powder blue",fg="black",command=equal).grid(row=5,column=3)

page.mainloop()


#Programmer:Fatemeh Golpour
