import calculatorDisplay

class ButtonsinArray():

    def __init__(self):
        self.buttonfuncs = calculatorDisplay.Buttonfunctions()
    
    def buttonFuncCall(self, i):
        myargs = [self.buttonfuncs.button1(), self.buttonfuncs.button2(), self.buttonfuncs.button3(), self.buttonfuncs.button4(), self.buttonfuncs.button5(), self.buttonfuncs.button6(), self.buttonfuncs.button7(), self.buttonfuncs.button8(), self.buttonfuncs.button9()]
        self.i = i
        myargs[self.i]
