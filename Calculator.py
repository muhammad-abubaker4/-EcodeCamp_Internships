import tkinter as tk

cal = ""

def add_calc(symbol):
    global cal
    cal += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, cal)

def eval_cal():
    global cal
    try:
        cal = str(eval(cal))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, cal)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global cal
    cal = ""
    text_result.delete(1.0, "end")

def delete_last():
    global cal
    cal = cal[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, cal)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.config(bg="lightgrey")

# Display area for calculator
text_result = tk.Text(root, height=2, width=25, font=("Arial", 24), borderwidth=5, relief="sunken", bg="white", fg="black")
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button configuration
button_width = 5
button_height = 2
font_style = ("Arial", 18)

# Button Styles
num_button_style = {"bg": "#f0f0f0", "fg": "black"}
op_button_style = {"bg": "#ffbf00", "fg": "black"}
special_button_style = {"bg": "#ff6666", "fg": "black"}

# Numeric Buttons
btn1 = tk.Button(root, text="1", command=lambda: add_calc(1), width=button_width, height=button_height, font=font_style, **num_button_style)
btn1.grid(column=0, row=3, padx=5, pady=5)
btn2 = tk.Button(root, text="2", command=lambda: add_calc(2), width=button_width, height=button_height, font=font_style, **num_button_style)
btn2.grid(column=1, row=3, padx=5, pady=5)
btn3 = tk.Button(root, text="3", command=lambda: add_calc(3), width=button_width, height=button_height, font=font_style, **num_button_style)
btn3.grid(column=2, row=3, padx=5, pady=5)

btn4 = tk.Button(root, text="4", command=lambda: add_calc(4), width=button_width, height=button_height, font=font_style, **num_button_style)
btn4.grid(column=0, row=4, padx=5, pady=5)
btn5 = tk.Button(root, text="5", command=lambda: add_calc(5), width=button_width, height=button_height, font=font_style, **num_button_style)
btn5.grid(column=1, row=4, padx=5, pady=5)
btn6 = tk.Button(root, text="6", command=lambda: add_calc(6), width=button_width, height=button_height, font=font_style, **num_button_style)
btn6.grid(column=2, row=4, padx=5, pady=5)

btn7 = tk.Button(root, text="7", command=lambda: add_calc(7), width=button_width, height=button_height, font=font_style, **num_button_style)
btn7.grid(column=0, row=5, padx=5, pady=5)
btn8 = tk.Button(root, text="8", command=lambda: add_calc(8), width=button_width, height=button_height, font=font_style, **num_button_style)
btn8.grid(column=1, row=5, padx=5, pady=5)
btn9 = tk.Button(root, text="9", command=lambda: add_calc(9), width=button_width, height=button_height, font=font_style, **num_button_style)
btn9.grid(column=2, row=5, padx=5, pady=5)

btn0 = tk.Button(root, text="0", command=lambda: add_calc(0), width=button_width, height=button_height, font=font_style, **num_button_style)
btn0.grid(column=1, row=6, padx=5, pady=5)

# Operation Buttons
btnplus = tk.Button(root, text="+", command=lambda: add_calc("+"), width=button_width, height=button_height, font=font_style, **op_button_style)
btnplus.grid(column=3, row=3, padx=5, pady=5)
btnminus = tk.Button(root, text="-", command=lambda: add_calc("-"), width=button_width, height=button_height, font=font_style, **op_button_style)
btnminus.grid(column=3, row=4, padx=5, pady=5)
btnmultiply = tk.Button(root, text="*", command=lambda: add_calc("*"), width=button_width, height=button_height, font=font_style, **op_button_style)
btnmultiply.grid(column=3, row=5, padx=5, pady=5)
btndiv = tk.Button(root, text="/", command=lambda: add_calc("/"), width=button_width, height=button_height, font=font_style, **op_button_style)
btndiv.grid(column=3, row=6, padx=5, pady=5)

# Special Buttons
btnequal = tk.Button(root, text="=", command=eval_cal, width=button_width, height=button_height, font=font_style, **op_button_style)
btnequal.grid(column=3, row=7, padx=5, pady=5)
btneopen = tk.Button(root, text="(", command=lambda: add_calc("("), width=button_width, height=button_height, font=font_style, **special_button_style)
btneopen.grid(column=0, row=6, padx=5, pady=5)
btneclose = tk.Button(root, text=")", command=lambda: add_calc(")"), width=button_width, height=button_height, font=font_style, **special_button_style)
btneclose.grid(column=2, row=6, padx=5, pady=5)
btnclear = tk.Button(root, text="Clear", command=clear_field, width=button_width, height=button_height, font=font_style, **special_button_style)
btnclear.grid(column=0, row=7, columnspan=2, padx=5, pady=5)
btnback = tk.Button(root, text="←", command=delete_last, width=button_width, height=button_height, font=font_style, **special_button_style)
btnback.grid(column=2, row=7, padx=5, pady=5)

root.mainloop()
