import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator - by ChiragAgg5k")
root.geometry("340x370")


def setText(s):
    textField.insert(tk.END, s)
    return


def evalText():
    try:
        eq = eval(textField.get())
    except SyntaxError:
        eq = ""

    textField.delete(0, tk.END)
    textField.insert(0, eq)

# Defining buttons

textField = tk.Entry(root, width=33, borderwidth=5)

button1 = tk.Button(text="1", padx=18, pady=18, command=lambda: setText("1"))
button2 = tk.Button(text="2", padx=18, pady=18, command=lambda: setText("2"))
button3 = tk.Button(text="3", padx=18, pady=18, command=lambda: setText("3"))
button4 = tk.Button(text="4", padx=18, pady=18, command=lambda: setText("4"))
button5 = tk.Button(text="5", padx=18, pady=18, command=lambda: setText("5"))
button6 = tk.Button(text="6", padx=18, pady=18, command=lambda: setText("6"))
button7 = tk.Button(text="7", padx=18, pady=18, command=lambda: setText("7"))
button8 = tk.Button(text="8", padx=18, pady=18, command=lambda: setText("8"))
button9 = tk.Button(text="9", padx=18, pady=18, command=lambda: setText("9"))
button0 = tk.Button(text="0", padx=18, pady=18, command=lambda: setText("0"))

buttonAdd = tk.Button(text="+", padx=18, pady=18, command=lambda: setText("+"))
buttonSub = tk.Button(text="-", padx=18, pady=18, command=lambda: setText("-"))
buttonMul = tk.Button(text="*", padx=18, pady=18, command=lambda: setText("*"))
buttonDiv = tk.Button(text="/", padx=18, pady=18, command=lambda: setText("/"))
buttonDec = tk.Button(text=".", padx=18, pady=18, command=lambda: setText("."))

buttonEq = tk.Button(text="=", padx=18, pady=18, command=evalText)
buttonClear = tk.Button(text="CLR", padx=50, pady=18,
                        command=lambda: textField.delete(0, tk.END))
buttonDel = tk.Button(text="DEL", padx=50, pady=18,
                      command=lambda: textField.delete(len(textField.get())-1, tk.END))

# Placing buttons

textField.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
buttonAdd.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonSub.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonMul.grid(row=3, column=3)

buttonDec.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttonEq.grid(row=4, column=2)
buttonDiv.grid(row=4, column=3)

buttonDel.grid(row=5, column=0, columnspan=2)
buttonClear.grid(row=5, column=2, columnspan=2)

root.mainloop()
