import random
import tkinter
from tkinter import *
import os
import calculatorMain

a = 0
b = 0

class Buttons():

    def __init__(self):
        self.a = 0
    

    def button1(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=1
            print(str(a))

    def button2(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=2
            print(str(a))

    def button3(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=3
            print(str(a))

    def button4(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=4
            print(str(a))
    

class GUI():
    def __init__(self):
        self.Buttons = Buttons()

    def buttons(self, root):
        buttonone = Button(frame, text="1", command = self.Buttons.button1)
        buttonone.pack()

        buttontwo = Button(frame, text="2", command = self.Buttons.button1)
        buttontwo.pack()

        buttonthree = Button(frame, text="3", command = self.Buttons.button1)
        buttonthree.pack()

        buttonfour = Button(frame, text="4", command = self.Buttons.button1)
        buttonfour.pack()

        buttonfive = Button(frame, text="5", command = self.Buttons.button1)
        buttonfive.pack()

        buttonsix = Button(frame, text="6", command = self.Buttons.button1)
        buttonsix.pack()

        buttonseven = Button(frame, text="7", command = self.Buttons.button1)
        buttonseven.pack()

        buttoneight = Button(frame, text="8", command = self.Buttons.button1)
        buttoneight.pack()

        buttonNine = Button(frame, text="9", command = self.Buttons.button1)
        buttonNine.pack()

        buttonzero = Button(frame, text="0", command = self.Buttons.button1)
        buttonzero.pack()


calculatorBrainInvoke = calculatorMain.Calculator()

buttons = Buttons()

root = tkinter.Tk()

calculatorBrainInvoke.calculate(2,3)

frame = Frame(root, height=540, width=500)
frame.pack()
bottomframe = Frame(root, height=540, width=500)
bottomframe.pack()

gui = GUI()
gui.buttons(root)

windowWidth = frame.winfo_reqwidth()
windowHeight = frame.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()







