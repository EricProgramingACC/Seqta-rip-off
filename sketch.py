import tkinter as tk
from tkinter import ttk

#window 
window=tk.Tk()
window.title('testing')
window.geometry('500x500')

#title
title_label=ttk.Label( master=window, text = 'testing' , font='calibri 24 bold')
title_label.pack()




#run
window.mainloop()