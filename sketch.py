#https://www.youtube.com/watch?v=RTM9tiV_HoY
#the new boston
import tkinter
from tkinter import*


root = Tk()
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)


button1=Button(topFrame, text="click 1", fg="red")
button2=Button(topFrame, text="click 2", fg="blue")
button3=Button(topFrame, text="click 3", fg="green")
button4=Button(bottomFrame, text="click 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack()

one =Label(root, text="one", bg="red",fg="white",)
one.pack()
two =Label(root, text="two", bg="black",fg="white",)
two.pack(fill=X)
three =Label(root, text="three", bg="black",fg="grey",)
three.pack(side=LEFT, fill=Y)

lable1=Label(root, text="gay")
lable2=Label(root, text="gay2")
entry1=Entry(root)
entry2=Entry(root)
entry1.grid(row=0,column=2)

root.mainloop()