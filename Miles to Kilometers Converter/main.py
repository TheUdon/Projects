from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

label1 = Label(text="is equal to", font=("Arial", 18))
label1.grid(column=0, row=1)

label2 = Label(text="Km", font=("Arial", 18))
label2.grid(column=2, row=1)

label3 = Label(text="Km", font=("Arial", 18))
label3.grid(column=2, row=1)

label3 = Label(text="Miles", font=("Arial", 18))
label3.grid(column=2, row=0)
label3.config(padx=10)

my_label = Label(text="0", font=("Arial", 18))
my_label.grid(column=1, row=1)
my_label.config(pady=10)


def button_clicked():
    conversion = round(int(input.get()) * 1.609)
    my_label["text"] = str(conversion)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=15)
input.grid(column=1, row=0)

window.mainloop()
