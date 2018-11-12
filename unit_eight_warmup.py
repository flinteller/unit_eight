import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

fer = tkinter.StringVar()

cel = tkinter.StringVar()


def f_to_c():
    fer_temp = int(fer.get())
    cel_temp = (5/9) * (fer_temp - 32)
    cel.set(str(cel_temp))


degree_f = tkinter.Label(root, text="degrees F:")
degree_f.grid(row=1, column=1)

f_entry = tkinter.Entry(root, textvariable=fer)
f_entry.grid(row=1, column=2)

degree_c = tkinter.Label(root, text="degrees C:")
degree_c.grid(row=2, column=1)

c_answer = tkinter.Label(root, textvariable=cel)
c_answer.grid(row=2, column=2)

convert_button = tkinter.Button(root, text="convert", command=f_to_c)
convert_button.grid(row=3, column=1)

root.mainloop()
