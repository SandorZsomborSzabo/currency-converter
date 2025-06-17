import tkinter as tk


"""
Logic for conversion between each currency
"""
def conversion():
    if opt1.get() == "EUR":
        if opt2.get() == "EUR":
            return float(textbox.get())
        elif opt2.get() == "USD":
            return float(textbox.get()) * 1.14
        elif opt2.get() == "GBP":
            return float(textbox.get()) * 0.85

    elif opt1.get() == "USD":
        if opt2.get() == "USD":
            return float(textbox.get())
        elif opt2.get() == "EUR":
            return float(textbox.get()) * 0.87
        elif opt2.get() == "GBP":
            return float(textbox.get()) * 0.74

    elif opt1.get() == "GBP":
        if opt2.get() == "GBP":
            return float(textbox.get())
        elif opt2.get() == "USD":
            return float(textbox.get()) * 1.34
        elif opt2.get() == "EUR":
            return float(textbox.get()) * 1.17

    return None

window = tk.Tk()

window.geometry("350x450")
window.title("Currency Converter")

label = tk.Label(window, text="Currency Converter", font=("Arial", 20))
label.pack(padx=10, pady=10)

textbox = tk.Entry(window, font = ("Arial", 16))
textbox.pack(padx=10, pady=10)

# Dropdown options
currency_from = ["EUR", "USD", "GBP"]

currency_to = ["EUR", "USD", "GBP"]

# Selected option variable
opt1 = tk.StringVar(value="EUR")
opt2 = tk.StringVar(value="EUR")

# Dropdown menu, from
tk.OptionMenu(window, opt1, *currency_from).place(x=50, y=120, height=40, width=100)
from_label = tk.Label(window, text="From", font=("Arial", 12)).place(x=70, y=100)

# Dropdown menu, to
tk.OptionMenu(window, opt2, *currency_to).place(x=200, y=120, height=40, width=100)
to_label = tk.Label(window, text="To", font=("Arial", 12)).place(x=230, y=100)

def print_result():
    result=tk.Label(window, text=f"Result is {conversion()}", bd=10, relief="solid").place(x=50, y=240, height=40, width=250)

convert = tk.Button(window, text="Convert", command=print_result).place(x=50, y=170, height=40, width=250)

window.mainloop()
