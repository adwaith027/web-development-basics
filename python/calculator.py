class Calculator:
    def __init__(self,a,b,opn):
        self.a=a
        self.b=b
        self.opn=opn
    
    def add(self):
        print(a+b)

    def sub(self):
        print(a-b)
    
    def mul(self):
        print(a*b)

    def dvd(self):
        print(a/b)

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
opn=str(input('operation(sum,diff,mult,div): '))

calculation=Calculator(a,b,opn)

if calculation.opn=='sum':
    ans=calculation.add()
    print(ans)
elif calculation.opn=='diff':
    ans=calculation.sub()
    print(ans)
elif calculation.opn=='mult':
    ans=calculation.mul()
    print(ans)
elif calculation.opn=='div':
    ans=calculation.dvd()
    print(ans)
else:
    print('Calulator error')