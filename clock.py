import tkinter as tk
from time import strftime

def Updat_time() :
    time = strftime("%H:%M:%S %p")
    lbl.config(text=time)
    lbl.after(1000, Updat_time)


clock =tk.Tk()

clock.title("DIGITAL COLCK")

lbl = tk.Label(clock,font=("lcd Solid",50,"bold"),background="pink",foreground="black")
lbl.pack(anchor="center")
Updat_time()
clock.mainloop()