from tkinter import *

window = Tk()


calcFrame = Frame(width='600',height='600')
calcFrame.pack()

#-------pantalla--------
screen = Entry(calcFrame)
screen.grid(row=1, column=1, padx=10, pady=10)
screen.config(background="black", fg="#03f943", justify="right")

#-----------fila 3 --------------
seven = Button(calcFrame, text='7', width=3)
seven.grid(row=2,column=1)

eight = Button(calcFrame, text='8', width=3)
eight.grid(row=2,column=2)

nine = Button(calcFrame, text='9', width=3)
nine.grid(row=2,column=3)

multiply = Button(calcFrame, text="x",width=3)
multiply.grid(row=3,column=4)





window.mainloop()