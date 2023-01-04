from tkinter import *

window = Tk()


calcFrame = Frame(width='600',height='600')
calcFrame.pack()

#-------pantalla--------
user = StringVar()
screen = Entry(calcFrame, textvariable=user)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")

#-----------fila 1 --------------
seven = Button(calcFrame, text='7', width=3)
seven.grid(row=2,column=1)

eight = Button(calcFrame, text='8', width=3)
eight.grid(row=2,column=2)

nine = Button(calcFrame, text='9', width=3)
nine.grid(row=2,column=3)

divide = Button(calcFrame, text="/",width=3)
divide.grid(row=2,column=4)

#---------------fila 2 ----------------

four = Button(calcFrame, text='4', width=3)
four.grid(row=3,column=1)

five = Button(calcFrame, text='5', width=3)
five.grid(row=3,column=2)

six = Button(calcFrame, text='6', width=3)
six.grid(row=3,column=3)

multiply = Button(calcFrame, text="x",width=3)
multiply.grid(row=3,column=4)

#---------------fila 3 ----------------

one = Button(calcFrame, text='1', width=3)
one.grid(row=4,column=1)

two = Button(calcFrame, text='2', width=3)
two.grid(row=4,column=2)

three = Button(calcFrame, text='3', width=3)
three.grid(row=4,column=3)

minus = Button(calcFrame, text="-",width=3)
minus.grid(row=4,column=4)

#---------------fila 4 ----------------

zero = Button(calcFrame, text='0', width=3)
zero.grid(row=5,column=1)

decimal = Button(calcFrame, text=',', width=3)
decimal.grid(row=5,column=2)

equals = Button(calcFrame, text="=",width=3)
equals.grid(row=5,column=3)

plus = Button(calcFrame, text='+', width=3)
plus.grid(row=5,column=4)

#-----function-----



def codigoBoton(entry):
    user.set()





window.mainloop()