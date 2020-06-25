import random
import tkinter
from tkinter import Button
from tkinter import Text
from tkinter import Label
#from tkinter import *
import os
import calculatorMain

a = 0
b = 1
c = 1

class Buttonfunctions():

    def __init__(self):
        self.calcmain = calculatorMain.Calculator()
        self.Buttonobj = ButtonObjects()
    

    def button1(self):
        global b
        global a
        global c
        if b <= 0:
            b +=1
        else:
            a *= 10
            a +=1
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
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
            self.Buttonobj.text(root)
            print(str(a))

    def equalbutton(self):
        global a
        global b
        global c
        self.calcmain.calculate(a,c)
        self.Buttonobj.text(root)
   
    
#i renamed it before but now it should probably be named back because the text is not a button...
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
                testbutton.place(height = 40, width = 40, x = 180 - 50 + 50*y, y = 490 + 50 - 50*x)


        buttonzero = Button(root, text="0", command = self.Buttons.button0)
        buttonzero.place(height=40,width=40,x=130,y=490)

        buttonEquals = Button(root, text="=", command = self.Buttons.equalbutton)
        buttonEquals.place(height=40,width=50, x = 120, y = 430)

    def text(self, root):
        w = Label(root, text=str(a))
        w.place(x=240, y = 50)



calculatorBrainInvoke = calculatorMain.Calculator()

root = tkinter.Tk()

root.title("Calculator")

root.geometry("500x540")

gui = ButtonObjects()
gui.buttons(root)
gui.text(root)

root.update_idletasks()

positionRight = int(710)
positionDown = int(270)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()








