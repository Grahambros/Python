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

    def button5(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=5
            print(str(a))

    def button6(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=6
            print(str(a))

    def button7(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=7
            print(str(a))

    def button8(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=8
            print(str(a))

    def button9(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=9
            print(str(a))

    def button0(self):
        global b
        global a
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=0
            print(str(a))
   
    

class GUI():
    def __init__(self):
        self.Buttons = Buttons()

    def buttons(self, root):
        buttonone = Button(root, text="1", command = self.Buttons.button1)
        buttonone.place(height=20,width=20,x=40,y=20)

        buttontwo = Button(root, text="2", command = self.Buttons.button2)
        buttontwo.pack()

        buttonthree = Button(root, text="3", command = self.Buttons.button3)
        buttonthree.pack(side = RIGHT)

        buttonfour = Button(root, text="4", command = self.Buttons.button4)
        buttonfour.pack(side = LEFT)

        buttonfive = Button(root, text="5", command = self.Buttons.button5)
        buttonfive.pack()

        buttonsix = Button(root, text="6", command = self.Buttons.button6)
        buttonsix.pack(side = RIGHT)

        buttonseven = Button(root, text="7", command = self.Buttons.button7)
        buttonseven.pack(side = LEFT)

        buttoneight = Button(root, text="8", command = self.Buttons.button8)
        buttoneight.pack()

        buttonNine = Button(root, text="9", command = self.Buttons.button9)
        buttonNine.pack(side = RIGHT)

        buttonzero = Button(root, text="0", command = self.Buttons.button0)
        buttonzero.pack()


calculatorBrainInvoke = calculatorMain.Calculator()

buttons = Buttons()

root = tkinter.Tk()

root.title("Calculator")

root.geometry("500x540")


gui = GUI()
gui.buttons(root)

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()


positionRight = int(710)
positionDown = int(270)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()








