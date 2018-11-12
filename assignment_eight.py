import tkinter

root = tkinter.Tk()
root.title("Calculator")

answer = tkinter.StringVar()


def nine():
    old_number = answer.get()
    new_number = old_number + "9"
    answer.set(new_number)


def eight():
    old_number = answer.get()
    new_number = old_number + "8"
    answer.set(new_number)


def seven():
    old_number = answer.get()
    new_number = old_number + "7"
    answer.set(new_number)


def six():
    old_number = answer.get()
    new_number = old_number + "6"
    answer.set(new_number)


def five():
    old_number = answer.get()
    new_number = old_number + "5"
    answer.set(new_number)


def four():
    old_number = answer.get()
    new_number = old_number + "4"
    answer.set(new_number)


def three():
    old_number = answer.get()
    new_number = old_number + "3"
    answer.set(new_number)


def two():
    old_number = answer.get()
    new_number = old_number + "2"
    answer.set(new_number)


def one():
    old_number = answer.get()
    new_number = old_number + "1"
    answer.set(new_number)


def zero():
    old_number = answer.get()
    new_number = old_number + "0"
    answer.set(new_number)


def plus():
    old_number = answer.get()
    new_number = old_number + "+"
    answer.set(new_number)


def minus():
    old_number = answer.get()
    new_number = old_number + "-"
    answer.set(new_number)


def mult():
    old_number = answer.get()
    new_number = old_number + "*"
    answer.set(new_number)


def div():
    old_number = answer.get()
    new_number = old_number + "/"
    answer.set(new_number)


def exp():
    old_number = answer.get()
    new_number = old_number + "**"
    answer.set(new_number)


def sqrt():
    old_number = float(answer.get())
    new_number = old_number ** .5
    answer.set(str(new_number))


def clear():
    answer.set("")


def enter():
    equation = answer.get()
    new = eval(equation)
    answer.set(new)


title_label = tkinter.Label(root, text="Calculator", font="helvetica 16 bold")
title_label.grid(row=0, column=2,)

answer_entry = tkinter.Entry(root, textvariable=answer)
answer_entry.grid(row=1, column=0, columnspan=5, ipadx=35)

nine_button = tkinter.Button(root, text="9", command=nine)
nine_button.grid(row=2, column=2, sticky="W", ipadx=5, ipady=3)

eight_button = tkinter.Button(root, text="8", command=eight)
eight_button.grid(row=2, column=1, ipadx=5, ipady=3)

seven_button = tkinter.Button(root, text="7", command=seven)
seven_button.grid(row=2, column=0, sticky="E", ipadx=5, ipady=3)

six_button = tkinter.Button(root, text="6", command=six)
six_button.grid(row=3, column=2, sticky="W", ipadx=5, ipady=3)

five_button = tkinter.Button(root, text="5", command=five)
five_button.grid(row=3, column=1, ipadx=5, ipady=3)

four_button = tkinter.Button(root, text="4", command=four)
four_button.grid(row=3, column=0, sticky="E", ipadx=5, ipady=3)

three_button = tkinter.Button(root, text="3", command=three)
three_button.grid(row=4, column=2, sticky="W", ipadx=5, ipady=3)

two_button = tkinter.Button(root, text="2", command=two)
two_button.grid(row=4, column=1, ipadx=5, ipady=3)

one_button = tkinter.Button(root, text="1", command=one)
one_button.grid(row=4, column=0, ipadx=5, ipady=3, sticky="E")

zero_button = tkinter.Button(root, text="0", command=zero)
zero_button.grid(row=5, column=0, ipadx=35, ipady=3, columnspan=3, sticky="W")

plus_button = tkinter.Button(root, text="+", command=plus)
plus_button.grid(row=2, column=3, ipadx=16, ipady=3, sticky="E")

minus_button = tkinter.Button(root, text="-", command=minus)
minus_button.grid(row=2, column=4, ipadx=16, ipady=3, sticky="W")

mult_button = tkinter.Button(root, text="x", command=mult)
mult_button.grid(row=3, column=3, ipadx=16, ipady=3, sticky="E")

div_button = tkinter.Button(root, text="/", command=div)
div_button.grid(row=3, column=4, ipadx=17, ipady=3, sticky="W")

exp_button = tkinter.Button(root, text="x^2", command=exp)
exp_button.grid(row=4, column=3, ipadx=9, ipady=3, sticky="E")

sqrt_button = tkinter.Button(root, text="√", command=sqrt)
sqrt_button.grid(row=4, column=4, ipadx=14, ipady=3, sticky="W")

clear_button = tkinter.Button(root, text="Clear", command=clear)
clear_button.grid(row=5, column=3, ipadx=3, ipady=3, sticky="E")

enter_button = tkinter.Button(root, text="Enter", command=enter)
enter_button.grid(row=5, column=4, ipadx=3, ipady=3, sticky="W")

root.mainloop()
