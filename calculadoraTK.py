from tkinter import *

window = Tk()


calcFrame = Frame(width='600',height='600')
calcFrame.pack()

#-------Screen--------
screenNumber = StringVar()

screen = Entry(calcFrame, textvariable=screenNumber)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")

#-------------------screen entries---------------
def entryNumber(entry):

    screenNumber.set(screenNumber.get() + entry)
#-----------Row 1 --------------
seven = Button(calcFrame, text='7', width=3, command=lambda:entryNumber("7"))
seven.grid(row=2,column=1)

eight = Button(calcFrame, text='8', width=3, command=lambda:entryNumber("8"))
eight.grid(row=2,column=2)

nine = Button(calcFrame, text='9', width=3, command=lambda:entryNumber("9"))
nine.grid(row=2,column=3)

divide = Button(calcFrame, text="/",width=3, command=entryNumber)
divide.grid(row=2,column=4)

#---------------Row 2 ----------------

four = Button(calcFrame, text='4', width=3, command=lambda:entryNumber("4"))
four.grid(row=3,column=1)

five = Button(calcFrame, text='5', width=3,command=lambda:entryNumber("5"))
five.grid(row=3,column=2)

six = Button(calcFrame, text='6', width=3, command=lambda:entryNumber("6"))
six.grid(row=3,column=3)

multiply = Button(calcFrame, text="x",width=3, command=entryNumber)
multiply.grid(row=3,column=4)

#---------------Row 3 ----------------

one = Button(calcFrame, text='1', width=3, command=lambda:entryNumber("3"))
one.grid(row=4,column=1)

two = Button(calcFrame, text='2', width=3, command=lambda:entryNumber("2"))
two.grid(row=4,column=2)

three = Button(calcFrame, text='3', width=3, command=lambda:entryNumber("1"))
three.grid(row=4,column=3)

minus = Button(calcFrame, text="-",width=3, command=entryNumber)
minus.grid(row=4,column=4)

#---------------Row 4 ----------------

zero = Button(calcFrame, text='0', width=3, command=lambda:entryNumber("0"))
zero.grid(row=5,column=1)

decimal = Button(calcFrame, text=',', width=3, command=lambda:entryNumber(","))
decimal.grid(row=5,column=2)

equals = Button(calcFrame, text="=",width=3, command=entryNumber)
equals.grid(row=5,column=3)

plus = Button(calcFrame, text='+', width=3, command=entryNumber)
plus.grid(row=5,column=4)

#-----function-----






window.mainloop()