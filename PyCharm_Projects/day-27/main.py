import tkinter


def calculate_clicked():
    miles_to_convert = float(entry_miles.get())
    calculated_kilometers = miles_to_convert * 1.6
    label_result.config(text=f"{calculated_kilometers:.2f}")

if __name__ == '__main__':
    window = tkinter.Tk()

    window.title("Mile to Km Converter")
    window.minsize(width=500, height=300)
    window['padx'] = 50
    window['pady'] = 50

    entry_miles = tkinter.Entry(width=10)
    entry_miles.grid(column=1, row=0)

    label_miles = tkinter.Label(text="Miles", font=("Arial", 20))
    label_miles.grid(column=2, row=0)
    label_miles.config(padx=10, pady=10)

    label_miles = tkinter.Label(text="is equal to", font=("Arial", 20))
    label_miles.grid(column=0, row=1)
    label_miles.config(padx=10, pady=10)

    label_result = tkinter.Label(text=" 0.00", font=("Arial", 20))
    label_result.grid(column=1, row=1)
    label_result.config(padx=10, pady=10)

    label_kilometer = tkinter.Label(text="Km", font=("Arial", 20))
    label_kilometer.grid(column=2, row=1)
    label_kilometer.config(padx=10, pady=10)

    button_calculate = tkinter.Button(text="Calculate", command=calculate_clicked)
    button_calculate.grid(column=1, row=2)
    button_calculate.config(padx=10, pady=10)


    window.mainloop()



