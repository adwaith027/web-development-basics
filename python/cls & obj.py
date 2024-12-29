class Microwave:
    def __init__(self,brand:str,power_rating:str,price:int):
        self.brand=brand
        self.power_rating=power_rating
        self.price=price
        self.status=False

    def turn_on(self):
        if self.status:   #this shows that status is true or that microwave is already turned on
            print(f'Microwave {self.brand} is already on')
        else:
            self.status=True
            print(f'Microwave {self.brand} is now turned on')

    def turn_off(self):
        if self.status:
            self.status=False
            print(f'Microwave {self.brand} is now turned off')
        else:
            print(f'Microwave {self.brand} is already turned off')
    

    def runmc(self,runtime):
        if self.status:
            print(f'Microwave {self.brand} ran for {runtime} minutes')
        else:
            print('Turn your microwave on')

    # def __mul__(self,other):
    #     return (f'{self.brand} * {other.brand}')

mcn1=Microwave('bosch','C',8000)

mcn2=Microwave('LG','C',7500)

# print(mcn1 * mcn2)

mcn1.turn_off()
mcn1.runmc(5)
mcn1.turn_on()
mcn1.runmc(2)
mcn1.turn_off()