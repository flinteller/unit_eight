import tkinter

root = tkinter.Tk()
root.title("Calculator")

title_label = tkinter.Label(root, text = "Calculator")
title_label.grid(row=0, column=1)

answer_entry = tkinter.Entry(root)
answer_entry.grid(row=1, column=1)

nine_button = tkinter.Button(root, text="9")
nine_button.grid(row=2, column=2)

eight_button = tkinter.Button(root, text="8")
eight_button.grid(row=2, column=1)

seven_button = tkinter.Button(root, text="7")
seven_button.grid(row=2, column=0)

six_button = tkinter.Button(root, text="6")
six_button.grid(row=3, column=2)

five_button = tkinter.Button(root, text="5")
five_button.grid(row=3, column=1)

four_button = tkinter.Button(root, text="4")
four_button.grid(row=3, column=0)

three_button = tkinter.Button(root, text="3")
three_button.grid(row=4, column=2)

two_button = tkinter.Button(root, text="2")
two_button.grid(row=4, column=1)

one_button = tkinter.Button(root, text="1")
one_button.grid(row=4, column=0)

zero_button = tkinter.Button(root, text="0")
zero_button.grid(row=5, column=1)

plus_button = tkinter.Button(root, text="+")
plus_button.grid(row=2, column=4)

minus_button = tkinter.Button(root, text="-")
minus_button.grid(row=2, column=5)

mult_button = tkinter.Button(root, text="x")
mult_button.grid(row=3, column=4)

div_button = tkinter.Button(root, text="/")
div_button.grid(row=3, column=5)

exp_button = tkinter.Button(root, text="x^2")
exp_button.grid(row=4, column=4)

sqrt_button = tkinter.Button(root, text="√")
sqrt_button.grid(row=4, column=5)

clear_button = tkinter.Button(root, text="Clear")
clear_button.grid(row=5, column=3)

enter_button = tkinter.Button(root, text="Enter")
enter_button.grid(row=5, column=4)

root.mainloop()
