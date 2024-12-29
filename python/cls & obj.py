class Microwave:
    def __init__(self,brand:str,power_rating:str,price:int):
        self.brand=brand
        self.power_rating=power_rating
        self.price=price
        self.status=False

    def turn_on(self):
        if self.status:   #it shows if status is true or microwave is already turned on
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

hello=Microwave('bosch','C',8000)

hello.turn_off()
hello.runmc(5)
hello.turn_on()
hello.runmc(2)
hello.turn_off()