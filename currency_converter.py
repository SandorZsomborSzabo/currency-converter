import tkinter as tk

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
tk.OptionMenu(window, opt1, *currency_from).place(x=50, y=100, height=40, width=100)

# Dropdown menu, to
tk.OptionMenu(window, opt2, *currency_to).place(x=200, y=100, height=40, width=100)

convert = tk.Button(window, text="Convert").place(x=50, y=150, height=40, width=250)


window.mainloop()