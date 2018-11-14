import tkinter

root = tkinter.Tk()
root.title("Calculator")

answer = tkinter.StringVar()


def nine():
    """
    adds 9 to the entry field
    :return: none
    """
    old_number = answer.get()
    new_number = old_number + "9"
    answer.set(new_number)


def eight():
    """
        adds 8 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "8"
    answer.set(new_number)


def seven():
    """
        adds 7 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "7"
    answer.set(new_number)


def six():
    """
        adds 6 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "6"
    answer.set(new_number)


def five():
    """
        adds 5 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "5"
    answer.set(new_number)


def four():
    """
        adds 4 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "4"
    answer.set(new_number)


def three():
    """
        adds 3 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "3"
    answer.set(new_number)


def two():
    """
        adds 2 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "2"
    answer.set(new_number)


def one():
    """
        adds 1 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "1"
    answer.set(new_number)


def zero():
    """
        adds 0 to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "0"
    answer.set(new_number)


def plus():
    """
        adds + to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "+"
    answer.set(new_number)


def minus():
    """
        adds - to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "-"
    answer.set(new_number)


def mult():
    """
        adds * to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "*"
    answer.set(new_number)


def div():
    """
        adds * to the entry field
        :return: none
        """
    old_number = answer.get()
    new_number = old_number + "/"
    answer.set(new_number)


def exp():
    """
    raises the previous number in the entry field to the power of 2
    :return: none
    """
    old_number = float(answer.get())
    new_number = old_number ** 2
    answer.set(str(new_number))


def sqrt():
    """
    raises the previous number in the entry field to the power of .5
    :return: none
    """
    old_number = float(answer.get())
    new_number = old_number ** .5
    answer.set(str(new_number))


def clear():
    """
    sets entry field to nothing
    :return: none
    """
    answer.set("")


def enter():
    """
    evaluates the string in the entry field 
    :return: none
    """
    equation = answer.get()
    new = eval(equation)
    answer.set(new)


answer_entry = tkinter.Entry(root, textvariable=answer, bg="orange1")
answer_entry.grid(row=1, column=0, columnspan=5, ipadx=35)

nine_button = tkinter.Button(root, text="9", command=nine, fg="chocolate1")
nine_button.grid(row=2, column=2, sticky="N,E,S,W", ipadx=5, ipady=3)

eight_button = tkinter.Button(root, text="8", command=eight, fg="chocolate1")
eight_button.grid(row=2, column=1, sticky="N,E,S,W")

seven_button = tkinter.Button(root, text="7", command=seven, fg="chocolate1")
seven_button.grid(row=2, column=0, sticky="N,E,S,W", ipadx=5, ipady=3)

six_button = tkinter.Button(root, text="6", command=six, fg="chocolate1")
six_button.grid(row=3, column=2, sticky="N,E,S,W", ipadx=5, ipady=3)

five_button = tkinter.Button(root, text="5", command=five, fg="chocolate1")
five_button.grid(row=3, column=1, ipadx=5, ipady=3, sticky="N,E,S,W")

four_button = tkinter.Button(root, text="4", command=four, fg="chocolate1")
four_button.grid(row=3, column=0, ipadx=5, ipady=3, sticky="N,E,S,W")

three_button = tkinter.Button(root, text="3", command=three, fg="chocolate1")
three_button.grid(row=4, column=2, ipadx=5, ipady=3, sticky="N,E,S,W")

two_button = tkinter.Button(root, text="2", command=two, fg="chocolate1")
two_button.grid(row=4, column=1, ipadx=5, ipady=3, sticky="N,E,S,W")

one_button = tkinter.Button(root, text="1", command=one, fg="chocolate1")
one_button.grid(row=4, column=0, ipadx=5, ipady=3, sticky="N,E,S,W")

zero_button = tkinter.Button(root, text="0", command=zero, fg="chocolate1")
zero_button.grid(row=5, column=0, ipadx=62, ipady=3, columnspan=3)

plus_button = tkinter.Button(root, text="+", command=plus, fg="chocolate1")
plus_button.grid(row=2, column=3, sticky="N,E,S,W")

minus_button = tkinter.Button(root, text="-", command=minus, fg="chocolate1")
minus_button.grid(row=2, column=4, sticky="N,E,S,W")

mult_button = tkinter.Button(root, text="x", command=mult, fg="chocolate1")
mult_button.grid(row=3, column=3, sticky="N,E,S,W")

div_button = tkinter.Button(root, text="/", command=div, fg="chocolate1")
div_button.grid(row=3, column=4, sticky="N,E,S,W")

exp_button = tkinter.Button(root, text="x^2", command=exp, fg="chocolate1")
exp_button.grid(row=4, column=3, sticky="N,E,S,W")

sqrt_button = tkinter.Button(root, text="√", command=sqrt, fg="chocolate1")
sqrt_button.grid(row=4, column=4, sticky="N,E,S,W")

clear_button = tkinter.Button(root, text="Clear", command=clear, fg="firebrick1")
clear_button.grid(row=5, column=3, sticky="N,E,S,W")

enter_button = tkinter.Button(root, text="Enter", command=enter, fg="firebrick1")
enter_button.grid(row=5, column=4, sticky="N,E,S,W")

root.mainloop()
