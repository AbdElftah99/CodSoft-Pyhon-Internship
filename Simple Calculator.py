import tkinter as tk
cal = ''

def addtocalc(symbol):
    global cal
    cal += str(symbol)
    text_result.delete(1.0 , "end")
    text_result.insert(1.0, cal)

def evaluate():
    global cal
    try:
        result = str(eval(cal))
        cal = ""
        text_result.delete(1.0 , "end")
        text_result.insert(1.0, result)
    except:    
        clear()
        text_result.insert(1.0, "Error!!")

def clear():
    global cal
    cal = ""
    text_result.delete(1.0 , "end") 


root = tk.Tk()
root.geometry("450x400")


text_result = tk.Text(root , height=3 , width=25 , font=("Arial", 24))
text_result.grid(columnspan=5)

#Numbers Buttons
btn_1 = tk.Button(root, text="1", command=lambda:addtocalc(1),width=7, font=("Arial", 15))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda:addtocalc(2),width=7, font=("Arial", 15))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda:addtocalc(3),width=7, font=("Arial", 15))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda:addtocalc(4),width=7, font=("Arial", 15))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda:addtocalc(5),width=7, font=("Arial", 15))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda:addtocalc(6),width=7, font=("Arial", 15))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda:addtocalc(7),width=7, font=("Arial", 15))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda:addtocalc(8),width=7, font=("Arial", 15))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda:addtocalc(9),width=7, font=("Arial", 15))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda:addtocalc(0),width=7, font=("Arial", 15))
btn_0.grid(row=5, column=3)

#Arthematic Operation Buttons
btn_plus = tk.Button(root, text="+", command=lambda:addtocalc("+"),width=7, font=("Arial", 15))
btn_plus.grid(row=2, column=4)

btn_min = tk.Button(root, text="-", command=lambda:addtocalc("-"),width=7, font=("Arial", 15))
btn_min.grid(row=3, column=4)

btn_mult = tk.Button(root, text="x", command=lambda:addtocalc("x"),width=7, font=("Arial", 15))
btn_mult.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda:addtocalc("/"),width=7, font=("Arial", 15))
btn_div.grid(row=5, column=4)

#other Buttons
btn_open = tk.Button(root, text="(", command=lambda:addtocalc("("),width=7, font=("Arial", 15))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda:addtocalc(")"),width=7, font=("Arial", 15))
btn_close.grid(row=5, column=2)

btn_clear = tk.Button(root, text="clear", command=clear,width=7, font=("Arial", 15))
btn_clear.grid(row=6, column=1)

btn_dot = tk.Button(root, text=".", command=lambda:addtocalc("."),width=7, font=("Arial", 15))
btn_dot.grid(row=6, column=2)

btn_eql = tk.Button(root, text="=", command=evaluate,width=7 , font=("Arial", 15))
btn_eql.grid(row=6, column=3)

root.mainloop()