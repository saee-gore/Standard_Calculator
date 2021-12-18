from tkinter import *
expression=""
#w is my root
w=Tk()
w.geometry("300x200")
w.resizable(0,0)
w.title("Standard Calculator")
equation = StringVar()
#functions
def press(item):
    global expression
    expression=expression+str(item)
    equation.set(expression)
def clear():
    global expression
    expression = ""
    equation.set("")
def equalbtn():
    try:
        global expression
        result=str(eval(expression))
        equation.set(result)
        expression=""
    except:
       equation.set("Error!")
       expression = ""
#end of functions
input_field=Entry(w,bd=4,textvariable=equation,justify = RIGHT)
input_field.grid(row=0,column=0)
input_field.pack()
btns_frame = Frame(w, width = 312, height = 273, bg = "grey")
seven=Button(btns_frame,text="7",command=lambda: press("7"))
eight=Button(btns_frame,text="8",command=lambda: press("8"))
nine=Button(btns_frame,text="9",command=lambda: press("9"))
plus=Button(btns_frame,text="+",command=lambda: press("+"))
four=Button(btns_frame,text="4",command=lambda: press("4"))
five=Button(btns_frame,text="5",command=lambda: press("5"))
six=Button(btns_frame,text="6",command=lambda: press("6"))
minus=Button(btns_frame,text="-",command=lambda: press("-"))
one=Button(btns_frame,text="1",command=lambda: press("1"))
two=Button(btns_frame,text="2",command=lambda: press("2"))
three=Button(btns_frame,text="3",command=lambda: press("3"))
division=Button(btns_frame,text="/", command=lambda: press("/"))
decimalpoint=Button(btns_frame,text=".",command=lambda: press("."))
zero=Button(btns_frame,text="0",command=lambda: press("0"))
multiply=Button(btns_frame,text="*",command=lambda: press("*"))
equalto=Button(btns_frame,text="=",command=equalbtn)
btns_frame.pack()
clear_frame=Frame(w, width = 312, height =50)
clear_btn=Button(clear_frame,text="Clear",command=clear)
clear_frame.pack()
#positions
seven.grid(row=1,column=0,padx = 1, pady = 1)
eight.grid(row=1,column=1,padx = 1, pady = 1)
nine.grid(row=1,column=2,padx = 1, pady = 1)
plus.grid(row=1,column=3,padx = 1, pady = 1)
four.grid(row=2,column=0,padx = 1, pady = 1)
five.grid(row=2,column=1,padx = 1, pady = 1)
six.grid(row=2,column=2,padx = 1, pady = 1)
minus.grid(row=2,column=3,padx = 1, pady = 1)
one.grid(row=3,column=0,padx = 1, pady = 1)
two.grid(row=3,column=1,padx = 1, pady = 1)
three.grid(row=3,column=2,padx = 1, pady = 1)
division.grid(row=3,column=3,padx = 1, pady = 1)
decimalpoint.grid(row=4,column=0,padx = 1, pady = 1)
zero.grid(row=4,column=1,padx = 1, pady = 1)
multiply.grid(row=4,column=2,padx = 1, pady = 1)
equalto.grid(row=4,column=3,padx = 1, pady = 1)
clear_btn.grid(row=5,column=0)
w.mainloop()
