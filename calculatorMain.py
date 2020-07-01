answer = 123457890
secondtime = False

class Calculator():

    def calculate(self, num1, num2, operationnum, true):
        global secondtime
        secondtime = true
        self.opn = operationnum
        if(self.opn == 1): division(num1, num2)
        if(self.opn == 2): multiplication(num1, num2)
        if(self.opn == 3): addition(num1, num2)
        if(self.opn == 4): subtraction(num1,num2)
        if(self.opn != 1 and self.opn != 2 and self.opn !=3 and self.opn != 4): print("no operator chosen!\n...or my code broke somehow")
        
        print(answer)

def division(num1, num2):
    global answer
    global secondtime
    if(secondtime != True): answer = num1/num2
    else: answer = num2/num1

#doesn't matter if this one is reversed or not
def multiplication(num1, num2):
    global answer
    answer = num1 * num2

#same with this one
def addition(num1, num2):
    global answer
    answer = num1 + num2

#but not this one
def subtraction(num1, num2):
    global answer
    global secondtime
    if(secondtime != True): answer = num1 - num2
    else: answer = num2 - num1