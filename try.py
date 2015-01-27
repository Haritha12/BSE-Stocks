import Tkinter as tk

master = tk.Tk()

var = tk.StringVar(master)

var.set("Day") 


option = tk.OptionMenu(master, var, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

option.pack()




def ok():
    
    Day = var.get()
    print Day


button = tk.Button(master, text="OK", command=ok)

button.pack()

master.mainloop()