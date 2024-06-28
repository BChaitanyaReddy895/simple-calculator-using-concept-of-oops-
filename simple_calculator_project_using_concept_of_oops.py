class Calculator:
    def __init__(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
    def addition(self):
        print(self.operand1+self.operand2)
    def subtraction(self):
        print(self.operand1-self.operand2)
    def multiplicaton(self):
        print(self.operand1*self.operand2)
    def division(self):
        if (self.operand2!=0):
            print(self.operand1/self.operand2)
        else:
            print("syntax error")
    def cal_remainder(self):
        print(self.operand1 % self.operand2)
obj1=Calculator(int(input("enter operand1:\n")),int(input("enter operand2:\n")))
operator=input("enter the operator(+,-,*,/,%):\n")
if operator=='+':
    print(obj1.addition())
elif operator=="-":

    print(obj1.subtraction())
elif operator=="*":
    print(obj1.multiplicaton())
elif operator=="/":
    print(obj1.division())
elif operator=="%":
    print(obj1.cal_remainder())
else:
    print("invalid operator")

        
        
