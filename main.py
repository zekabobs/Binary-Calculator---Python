from tkinter import *

#add number on display
def add(event):
    display.insert(len(display.get()),event.widget.cget('text'))

#reset display
def reset(event):
    display.delete(0,END)

#choose operation
def operation(event):
    global firstOperand
    global binOperation
    if not(display.get() == "") and binOperation == '':
        firstOperand = int(display.get(),2)
        display.delete(0, END)
        binOperation = event.widget.cget('text')
    elif binOperation != '':
        binOperation = event.widget.cget('text')
        
#calculate 
def calculate(event):
    global firstOperand
    global secondOperand
    global binOperation
    if binOperation != '' and firstOperand == 0:    
        display.delete(0,END)
    elif binOperation == '+' and (not(display.get() == '')):
        secondOperand = int(display.get(),2)
        display.delete(0,END)
        display.insert(0,format(firstOperand+secondOperand,'b'))
    elif binOperation == '*' and (not(display.get() == '')):
        secondOperand = int(display.get(),2)
        display.delete(0,END)
        display.insert(0,format(firstOperand*secondOperand,'b'))
    firstOperand = 0
    secondOperand = 0
    binOperation = ''

w = Tk()
w.geometry("300x240")
w.title("Calculator")

#constant window size
w.resizable(False, False)

#wrapper
c = Canvas(w,width=300,height=240)
c.pack()
c.create_rectangle(10,10,290,230,fill="papayawhip",width=2)
c.create_rectangle(20,20,280,50,fill="black",width=2)

#textbox
display = Entry(w,width=23,font="Arial 14",justify=RIGHT)
display.place(x=21,y=22)

#all buttons
zero  = Button(w,text="0",width=5,height=2,font="Arial 18",relief=GROOVE,bg="pink",activebackground="pink")
one   = Button(w,text="1",width=5,height=2,font="Arial 18",relief=GROOVE,bg="pink",activebackground="pink")
summ   = Button(w,text="+",width=5,height=2,font="Arial 18",relief=GROOVE,bg="pink",activebackground="pink")
mult  = Button(w,text="*",width=5,height=2,font="Arial 18",relief=GROOVE,bg="pink",activebackground="pink")
calc  = Button(w,text="=",width=5,height=2,font="Arial 18",relief=GROOVE,bg="pink",activebackground="pink")
res     = Button(w,text="C",width=5,height=2,font="Arial 18",relief=GROOVE,bg="pink",activebackground="pink")

zero.place(x=20,y=60)
one.place(x=110,y=60)
res.place(x=200,y=60)

summ.place(x=20,y=145)
mult.place(x=110,y=145)
calc.place(x=200,y=145)

#events
zero.bind("<Button-1>",add)
one.bind("<Button-1>",add)
res.bind("<Button-1>",reset)
mult.bind("<Button-1>",operation)
summ.bind("<Button-1>",operation)
calc.bind("<Button-1>",calculate)

firstOperand = 0
secondOperand = 0
binOperation = ''
flag = False

w.mainloop()
