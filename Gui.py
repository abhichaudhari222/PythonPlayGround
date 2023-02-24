from tkinter import *
window = Tk()
window.title("Rock Paper Scissors Game")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
# lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():

    lbl.configure(text="Name Submitted")

btn = Button(window,width=10, text="Click Me", command=clicked)

btn.grid(column=10, row=0)
window.mainloop()