import random
import tkinter
from tkinter import *
import os

root = tkinter.Tk()

whyisthishard = Calculator()

whyisthishard.calculate(1,2)


C = tkinter.Canvas(root, bg="black", height=580, width=1028)


frame = Frame(root)
frame.pack()

# Gets the requested values of the height and widht.
windowWidth = C.winfo_reqwidth()
windowHeight = C.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(C.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(C.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

C.pack()
root.mainloop()






operateNum = 0

class Calculator():
     def calculate(self, num1, num2):
         self.num1 = num1
         self.num2 = num2
         switcher = {
        0: "nothing",
        1: "division",
        2: "multiplication",
        3: "addition",
        4: "subtraction",
         }
         print(switcher.get(operateNum))

#hellow