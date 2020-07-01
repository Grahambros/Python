answer = 0
secondtime = False

class Calculator():

    def calculate(self, num1, num2, operationnum, true):
        global answer
        global secondtime
        secondtime = true
        self.opn = operationnum
        answer = num1
        self.list = [nothing(num1), division(num1, num2), multiplication(num1, num2), addition(num1, num2), subtraction(num1, num2)]
        self.list[self.opn]
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

def nothing(num1):
    print("idk why this runs everytime wait yes i do")