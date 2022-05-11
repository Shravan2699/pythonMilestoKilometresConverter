from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)
window.config(pady=20,padx=60)


my_label = Label(text="")
my_label.grid(column=0,row=0)

num_input = Entry(width=10)
num_input.grid(column=1,row=0)
num_input.config()

labl1 = Label(text="is equal to",font=("Arial",10))
labl1.grid(column=0,row=1)

labl2 = Label(text="Miles",font=("Arial",10))
labl2.grid(column=2,row=0)

answer = Label(text="0",font=("Arial",10))
answer.grid(column=1,row=1)

labl3 = Label(text="Km",font=("Arial",10))
labl3.grid(column=2,row=1)


def btn_clicked():
    input_display = int(num_input.get())
    answer.config(text=f"{round(input_display*1.609,2)}")

btn = Button(bg="grey",text="Calculate",command=btn_clicked)
btn.grid(column=1,row=2)



window.mainloop()