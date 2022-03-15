#graafilineyl5
#henri lepik
#08.03.22


from tkinter import *

#akena
aken = Tk()
aken.title('Nupps')
aken.geometry("300x200")


def summa():
    global protsent
    global uldse
    uldse = int(sisestus.get())
    protsent = int(var.get())
    kaibemaks = (uldse/100*protsent)
    hind = (uldse+kaibemaks)
    valjund2.config(text=f"{kaibemaks}€")
    valjund3.config(text=f"{hind}€")
    
    
#silt
silt = Label(aken, text="Hind ilma käibemaksuta:")
silt.grid(row=0,column=0)
valjund = Label(aken, text="------------------------------------------------------------------")
valjund.grid(row=6,columnspan=3)
valjund = Label(aken, text="Käibemaksu määr:")
valjund.grid(row=4,column=0)
valjund = Label(aken, text="Käibemaks:")
valjund.grid(row=7,column=0)
valjund2 = Label(aken, text="")
valjund2.grid(row=7,column=1)
valjund = Label(aken, text="Hind koos käibemaksuga:")
valjund.grid(row=8,column=0)
valjund3 = Label(aken, text="")
valjund3.grid(row=8,column=1)

#sisestamis koht
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

nupp1 = Button(aken, text="Kalkuta vastus", width=10, command=summa)
nupp1.grid(row=9, column=1)

#valik
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9)
valikukast.grid(row=4, column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20)
valikukast.grid(row=5, column=1)

aken.mainloop()

