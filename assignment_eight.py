import tkinter

root = tkinter.Tk()
root.title("Calculator")

answer = tkinter.StringVar()


def nine():
    old_number = answer.get()
    new_number = old_number + "9"
    answer.set(new_number)


title_label = tkinter.Label(root, text="Calculator")
title_label.grid(row=0, column=1)

answer_entry = tkinter.Entry(root, textvariable=answer)
answer_entry.grid(row=1, column=1)

nine_button = tkinter.Button(root, text="9", command=nine)
nine_button.grid(row=2, column=2)

eight_button = tkinter.Button(root, text="8", command=eight)
eight_button.grid(row=2, column=1)

seven_button = tkinter.Button(root, text="7", command=seven)
seven_button.grid(row=2, column=0)

six_button = tkinter.Button(root, text="6", command=six)
six_button.grid(row=3, column=2)

five_button = tkinter.Button(root, text="5", command=five)
five_button.grid(row=3, column=1)

four_button = tkinter.Button(root, text="4", command=four)
four_button.grid(row=3, column=0)

three_button = tkinter.Button(root, text="3", command=three)
three_button.grid(row=4, column=2)

two_button = tkinter.Button(root, text="2", command=two)
two_button.grid(row=4, column=1)

one_button = tkinter.Button(root, text="1", command=one)
one_button.grid(row=4, column=0)

zero_button = tkinter.Button(root, text="0", command=zero)
zero_button.grid(row=5, column=1)

plus_button = tkinter.Button(root, text="+", command=plus)
plus_button.grid(row=2, column=4)

minus_button = tkinter.Button(root, text="-", command=minus)
minus_button.grid(row=2, column=5)

mult_button = tkinter.Button(root, text="x", command=mult)
mult_button.grid(row=3, column=4)

div_button = tkinter.Button(root, text="/", command=div)
div_button.grid(row=3, column=5)

exp_button = tkinter.Button(root, text="x^2", command=exp)
exp_button.grid(row=4, column=4)

sqrt_button = tkinter.Button(root, text="√", command=sqrt)
sqrt_button.grid(row=4, column=5)

clear_button = tkinter.Button(root, text="Clear", command=clear)
clear_button.grid(row=5, column=3)

enter_button = tkinter.Button(root, text="Enter", command=enter)
enter_button.grid(row=5, column=4)

root.mainloop()
