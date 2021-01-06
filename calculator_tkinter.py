from tkinter import *


window = Tk()
window.title("Kalkulačka")
window.configure(bg='yellow')

#entry label
e = Entry(window, width=40, borderwidth=3)
e.grid(column=0, row=0, columnspan=5, pady=10, padx=10, ipady=10)


#def
def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)
def deduct():
    first_number = e.get()
    global f_num
    global math
    math = "deduct"
    f_num = int(first_number)
    e.delete(0, END)
def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)
def divide():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)
def equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "add":
        e.insert(0, f_num + int(second_number))
    elif math == "deduct":
        e.insert(0, f_num - int(second_number))
    elif math == "multiply":
        e.insert(0, f_num * int(second_number))
    elif math == "divide":
        e.insert(0, f_num / int(second_number))
    else:
        return



btn1 = Button(window, text="1", padx=30, pady=20, command=lambda: click(1))
btn2 = Button(window, text="2", padx=30, pady=20, command=lambda: click(2))
btn3 = Button(window, text="3", padx=30, pady=20, command=lambda: click(3))
btn4 = Button(window, text="4", padx=30, pady=20, command=lambda: click(4))
btn5 = Button(window, text="5", padx=30, pady=20, command=lambda: click(5))
btn6 = Button(window, text="6", padx=30, pady=20, command=lambda: click(6))
btn7 = Button(window, text="7", padx=30, pady=20, command=lambda: click(7))
btn8 = Button(window, text="8", padx=30, pady=20, command=lambda: click(8))
btn9 = Button(window, text="9", padx=30, pady=20, command=lambda: click(9))

btn_clear = Button(window, text="C", padx=30, pady=20, command=clear)
btn_add = Button(window, text="+", padx=30, pady=20, command=add)
btn_deduct = Button(window, text="-", padx=31, pady=20, command=deduct)
btn_divide = Button(window, text="/", padx=30, pady=20, command=divide)
btn_multiply = Button(window, text="*", padx=30, pady=20, command=multiply)
btn_equal = Button(window, text="=", padx=28, pady=50, command=equal)



#grid
btn7.grid(column=0, row=2, sticky="nsew")
btn8.grid(column=1, row=2, sticky="nsew")
btn9.grid(column=2, row=2, sticky="nsew")

btn4.grid(column=0, row=3, sticky="nsew")
btn5.grid(column=1, row=3, sticky="nsew")
btn6.grid(column=2, row=3, sticky="nsew")

btn1.grid(column=0, row=4, sticky="nsew")
btn2.grid(column=1, row=4, sticky="nsew")
btn3.grid(column=2, row=4, sticky="nsew")

btn_clear.grid(column=0, row=1, sticky="nsew")
btn_add.grid(column=1, row=1, sticky="nsew")
btn_deduct.grid(column=2, row=1, sticky="nsew")
btn_divide.grid(column=4, row=1, sticky="nsew")
btn_multiply.grid(column=4, row=2, sticky="nsew")
btn_equal.grid(column=4, row=3, rowspan=2, sticky="nsew")


window.mainloop()
