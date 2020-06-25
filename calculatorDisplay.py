import random
import tkinter
from tkinter import Button
#from tkinter import *
import os
import calculatorMain

a = 0
b = 1
c = 0

class Buttonfunctions():

    def __init__(self):
        self.calcmain = calculatorMain.Calculator()
    

    def button1(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=1
            print(str(a))

    def button2(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=2
            print(str(a))

    def button3(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=3
            print(str(a))

    def button4(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=4
            print(str(a))

    def button5(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=5
            print(str(a))

    def button6(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=6
            print(str(a))

    def button7(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=7
            print(str(a))

    def button8(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=8
            print(str(a))

    def button9(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=9
            print(str(a))

    def button0(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=0
            print(str(a))

    def equalbutton(self):
        global a
        global b
        global c
        if b <=0:
            b+=1
        else:
            self.calcmain.calculate(a,c)
   
    

class ButtonObjects():
    def __init__(self):
        self.Buttons = Buttonfunctions()
        self.i = 0
        self.myargs = [self.Buttons.button0, self.Buttons.button1, self.Buttons.button2, self.Buttons.button3, self.Buttons.button4, self.Buttons.button5, self.Buttons.button6, self.Buttons.button7, self.Buttons.button8, self.Buttons.button9]

    def buttons(self, root):

        for x in range(1, 4):
            for y in range(1,4):
                self.i+=1
                testbutton = Button(root, text=str(self.i), command = self.myargs[self.i])
                testbutton.place(height = 40, width = 40, x = 20 - 50 + 50*y, y = 30 - 50 + 50*x)

        buttonone = Button(root, text="1", command = self.Buttons.button1)
        buttonone.place(height=40,width=40,x=180,y=490)

        buttontwo = Button(root, text="2", command = self.Buttons.button2)
        buttontwo.place(height=40,width=40,x=230,y=490)

        buttonthree = Button(root, text="3", command = self.Buttons.button3)
        buttonthree.place(height=40,width=40,x=280,y=490)

        buttonfour = Button(root, text="4", command = self.Buttons.button4)
        buttonfour.place(height=40,width=40,x=180,y=440)

        buttonfive = Button(root, text="5", command = self.Buttons.button5)
        buttonfive.place(height=40,width=40,x=230,y=440)

        buttonsix = Button(root, text="6", command = self.Buttons.button6)
        buttonsix.place(height=40,width=40,x=280,y=440)

        buttonseven = Button(root, text="7", command = self.Buttons.button7)
        buttonseven.place(height=40,width=40,x=180,y=390)

        buttoneight = Button(root, text="8", command = self.Buttons.button8)
        buttoneight.place(height=40,width=40,x=230,y=390)

        buttonNine = Button(root, text="9", command = self.Buttons.button9)
        buttonNine.place(height=40,width=40,x=280,y=390)

        buttonzero = Button(root, text="0", command = self.Buttons.button0)
        buttonzero.place(height=40,width=40,x=130,y=490)


calculatorBrainInvoke = calculatorMain.Calculator()

buttons = Buttonfunctions()

root = tkinter.Tk()

root.title("Calculator")

root.geometry("500x540")


gui = ButtonObjects()
gui.buttons(root)


positionRight = int(710)
positionDown = int(270)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()








