import random
import tkinter
from tkinter import Button
from tkinter import Text
from tkinter import Label
import calculatorOperations

a = 0
b = 0

#the b stands for button. bool that checks if a button that controls an operation has been pressed
isoperatebpressed = False


#This class is a mess because i had to make different functions for all the buttons.
# I tried to make only one function, but it didn't work for some reason. i heard functools.partial could work but it wasn't and neither was lambda(it would give all same values for each button)
class Buttonfunctions():

    def __init__(self):
        self.calcmain = calculatorOperations
        self.calcfuncs = calculatorOperations.Calculator()
        self.operationnum = int
        self.w = Label(root, text=str(a))
        self.w.place(x=240, y = 50)
    

    def button1(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=1
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=1
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button2(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=2
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=2
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button3(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=3
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=3
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button4(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=4
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=4
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button5(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=5
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=5
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button6(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=6
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=6
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button7(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=7
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=7
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button8(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=8
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=8
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button9(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            a +=9
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            b +=9
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def button0(self):
        global b
        global a
        if(isoperatebpressed != True):
            a *= 10
            self.w.config(text=str(a))
            print(a)
        else:
            b *= 10
            self.w.config(text=str(b))
            print(b)
        self.w.place(x=240, y = 50)

    def equalbutton(self):
        global a
        global b
        global isoperatebpressed
        self.calcfuncs.calculate(a,b, self.operationnum)
        a = self.calcmain.answer 
        b = 0
        self.w.config(text=str(a))
        self.w.place(x=240, y = 50)

    def multiplicationButton(self):
        global a
        global b
        global isoperatebpressed
        isoperatebpressed = True
        self.operationnum = 2
        self.w.config(text=str(b))
        return isoperatebpressed

    def divisionButton(self):
        global a
        global b
        global isoperatebpressed
        isoperatebpressed = True
        self.operationnum = 1
        self.w.config(text=str(b))
        return isoperatebpressed

    def additionButton(self):
        global a
        global b
        global isoperatebpressed
        isoperatebpressed = True
        self.operationnum = 3
        self.w.config(text=str(b))
        return isoperatebpressed

    def subtractionButton(self):
        global a
        global b
        global isoperatebpressed
        isoperatebpressed = True
        self.operationnum = 4
        self.w.config(text=str(b))
        return isoperatebpressed

   
   
#i need a way to disable the numbered buttons when the equals button is pressed
class ButtonObjects():
    def __init__(self):
        self.Buttons = Buttonfunctions()
        self.i = 0
        self.myargs = [self.Buttons.button0, self.Buttons.button1, self.Buttons.button2, self.Buttons.button3, self.Buttons.button4, self.Buttons.button5, self.Buttons.button6, self.Buttons.button7, self.Buttons.button8, self.Buttons.button9]
        self.myoperators = [self.Buttons.button0, self.Buttons.divisionButton, self.Buttons.multiplicationButton, self.Buttons.additionButton, self.Buttons.subtractionButton]

    def buttons(self, root):
        self.text = ["help","÷", "x", "+", "-"]
        self.u = 0
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

        for t in range(0, 2):
            t+= 1
            for r in range(0,2):
                r+= 1
                self.u += 1
                operationbutton = Button(root, text=self.text[self.u], command = self.myoperators[self.u])
                operationbutton.place(height=40,width=40, x = 120-(50*t), y = 380+(50*r))
            

root = tkinter.Tk()
root.title("Calculator")
root.geometry("500x540")

# Positions the window in the center of the page.
root.geometry("+710+270")

gui = ButtonObjects()
gui.buttons(root)

root.mainloop()