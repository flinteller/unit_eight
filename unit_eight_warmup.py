import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

fer = tkinter.StringVar()

cel = tkinter.StringVar()

degree_f = tkinter.Label(root, text="degrees F:")
degree_f.grid(row=1, column=1)

f_entry = tkinter.Entry(root, textvariable=fer)
f_entry.grid(row=1, column=2)

degree_c = tkinter.Label(root, text="degrees C:")
degree_c.grid(row=2, column=1)



root.mainloop()
