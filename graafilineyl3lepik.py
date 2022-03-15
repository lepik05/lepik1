#ylesanne 10
#henri lepik
#08.03.22

from tkinter import *

#aknena
aken = Tk()
aken.title('Tkinter "Hello World"')
aken.geometry("400x150")
aken.resizable(0, 0)

#kasti kiri
lorem = 'Nimi: Henri lepik'
lorem2 = 'Rühm: IT-21'
lorem3 = '2022'

Label(aken, text=lorem, foreground="pink", background="green", padx=30, font="Tahoma 26 bold italic").pack()
Label(aken, text=lorem2, foreground="orange", background="blue", padx=300, font="Tahoma 26 bold italic").pack()
Label(aken, text=lorem3, foreground="pink", background="green",pady=10, padx=300, font="Tahoma 26 bold italic").pack()




aken.mainloop()