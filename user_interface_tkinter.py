# user_interface_tkinter.py
from tkinter import *


class Calculator:
    prev_val = 0

    def __init__(self, parent):
        self.create_widget(parent)
        self.special_buttons = ["Clear", "Sum", "Equal", "Coma", "Negative", "Percent", "Multiply", "Divide", "Substract"]

    def num_clicked(self, button_val):
        if button_val not in self.special_buttons:
            # self.display.delete(0, END)
            self.display.insert(0, button_val)
        else:
            if button_val == "Equal":
                cur_val = int(self.display.get())
                self.display.delete(0, END)

                if self.operation == "Sum":
                    result = cur_val + self.prev_val
                elif self.operation == "Substract":
                    result = self.prev_val - cur_val
                elif self.operation == "Multiply":
                    result = self.prev_val * cur_val
                elif self.operation == "Divide":
                    result = self.prev_val / cur_val

                # print(f"cur_val:{cur_val} prev_val:{self.prev_val} result:{result}")
                self.display.insert(0, result)
            else:
                self.prev_val = int(self.display.get())
                self.display.delete(0, END)
                self.operation = button_val
                if button_val == "Clear":
                    self.prev_val = 0
                elif button_val == "Negative":
                    self.prev_val *= -1
                    self.display.insert(0, self.prev_val)
                elif button_val == "Percent":
                    self.prev_val *= 0.01
                    self.display.insert(0, self.prev_val)

    def create_widget(self, root):
        root.title("Calculator")
        self.display = Entry(root)
        self.display.grid(row=0, columnspan=4)

        button_0 = Button(root, text="0", command=lambda: self.num_clicked(0), padx=90, pady=20, highlightbackground='#3E4149')
        button_1 = Button(root, text="1", command=lambda: self.num_clicked(1), padx=40, pady=20, highlightbackground='#3E4149')
        button_2 = Button(root, text="2", command=lambda: self.num_clicked(2), padx=40, pady=20, highlightbackground='#3E4149')
        button_3 = Button(root, text="3", command=lambda: self.num_clicked(3), padx=40, pady=20, highlightbackground='#3E4149')
        button_4 = Button(root, text="4", command=lambda: self.num_clicked(4), padx=40, pady=20, highlightbackground='#3E4149')
        button_5 = Button(root, text="5", command=lambda: self.num_clicked(5), padx=40, pady=20, highlightbackground='#3E4149')
        button_6 = Button(root, text="6", command=lambda: self.num_clicked(6), padx=40, pady=20, highlightbackground='#3E4149')
        button_7 = Button(root, text="7", command=lambda: self.num_clicked(7), padx=40, pady=20, highlightbackground='#3E4149')
        button_8 = Button(root, text="8", command=lambda: self.num_clicked(8), padx=40, pady=20, highlightbackground='#3E4149')
        button_9 = Button(root, text="9", command=lambda: self.num_clicked(9), padx=40, pady=20, highlightbackground='#3E4149')

        button_coma = Button(root, text=",", command=lambda: self.num_clicked("Coma"), padx=40, pady=20, highlightbackground='#3E4149')
        button_clr = Button(root, text="AC", command=lambda: self.num_clicked("Clear"), padx=40, pady=20, highlightbackground='#17202A')
        button_neg = Button(root, text="+/-", command=lambda: self.num_clicked("Negative"), padx=40, pady=20, highlightbackground='#17202A')
        button_per = Button(root, text="%", command=lambda: self.num_clicked("Percent"), padx=40, pady=20, highlightbackground='#17202A')
        button_div = Button(root, text="/", command=lambda: self.num_clicked("Divide"), padx=40, pady=20, highlightbackground='#FF4500')
        button_mul = Button(root, text="*", command=lambda: self.num_clicked("Multiply"), padx=40, pady=20, highlightbackground='#FF4500')
        button_sub = Button(root, text="-", command=lambda: self.num_clicked("Substract"), padx=40, pady=20, highlightbackground='#FF4500')
        button_pls = Button(root, text="+", command=lambda: self.num_clicked("Sum"), padx=40, pady=20, highlightbackground='#FF4500')
        button_equ = Button(root, text="=", command=lambda: self.num_clicked("Equal"), padx=40, pady=20, highlightbackground='#FF4500')

        button_0.grid(row=5, column=0, columnspan=2)
        button_1.grid(row=4, column=0)
        button_2.grid(row=4, column=1)
        button_3.grid(row=4, column=2)
        button_4.grid(row=3, column=0)
        button_5.grid(row=3, column=1)
        button_6.grid(row=3, column=2)
        button_7.grid(row=2, column=0)
        button_8.grid(row=2, column=1)
        button_9.grid(row=2, column=2)
        button_coma.grid(row=5, column=2)
        button_clr.grid(row=1, column=0)
        button_neg.grid(row=1, column=1)
        button_per.grid(row=1, column=2)
        button_div.grid(row=1, column=3)
        button_mul.grid(row=2, column=3)
        button_sub.grid(row=3, column=3)
        button_pls.grid(row=4, column=3)
        button_equ.grid(row=5, column=3)


if __name__ == '__main__':
    root = Tk()
    calc = Calculator(root)
    root.mainloop()
