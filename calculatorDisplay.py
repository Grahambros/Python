import random
import tkinter
from tkinter import Button
from tkinter import Text
from tkinter import Label
#from tkinter import *
import os
import calculatorMain

a = 0
b = 100
c = 0

class Buttonfunctions():

    def __init__(self):
        self.calcmain = calculatorMain.Calculator()
        self.w = Label(root, text=str(a))
        self.w.place(x=240, y = 50)
    

    def button1(self):
        global b
        global a
        global c
        a *= 10
        a +=1
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button2(self):
        global b
        global a
        global c
        a *= 10
        a +=2
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button3(self):
        global b
        global a
        global c
        a *= 10
        a +=3
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button4(self):
        global b
        global a
        global c
        a *= 10
        a +=4
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button5(self):
        global b
        global a
        global c
        a *= 10
        a +=5
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button6(self):
        global b
        global a
        global c
        a *= 10
        a +=6
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button7(self):
        global b
        global a
        global c
        a *= 10
        a +=7
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button8(self):
        global b
        global a
        global c
        a *= 10
        a +=8
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button9(self):
        global b
        global a
        global c
        a *= 10
        a +=9
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def button0(self):
        global b
        global a
        global c
        a *= 10
        a +=0
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
        print(str(a))

    def equalbutton(self):
        global a
        global b
        global c
        print(str(a+b))
        self.calcmain.calculate(a,c)
        self.w = Label(root, text=(str(a)))
        self.w.place(x=240, y = 50)
   
   
#i need a way to disable the numbered buttons when the equals button is pressed
class ButtonObjects():
    def __init__(self):
        self.Buttons = Buttonfunctions()
        self.i = 0
        self.myargs = [self.Buttons.button0, self.Buttons.button1, self.Buttons.button2, self.Buttons.button3, self.Buttons.button4, self.Buttons.button5, self.Buttons.button6, self.Buttons.button7, self.Buttons.button8, self.Buttons.button9]

    def buttons(self, root):
        numberedbutton = Button()
        for x in range(1, 4):
            for y in range(1,4):
                self.i+=1
                numberedbutton = Button(root, text=str(self.i), command = self.myargs[self.i])
                numberedbutton.place(height = 40, width = 40, x = 180 - 50 + 50*y, y = 490 + 50 - 50*x)


        buttonzero = Button(root, text="0", command = self.Buttons.button0)
        buttonzero.place(height=40,width=40,x=130,y=490)

        buttonEquals = Button(root, text="=", command = self.Buttons.equalbutton)
        buttonEquals.place(height=40,width=50, x = 120, y = 430)



calculatorBrainInvoke = calculatorMain.Calculator()

root = tkinter.Tk()

root.title("Calculator")

root.geometry("500x540")

gui = ButtonObjects()
gui.buttons(root)


root.update_idletasks()


# Positions the window in the center of the page.
root.geometry("+710+270")

root.mainloop()








