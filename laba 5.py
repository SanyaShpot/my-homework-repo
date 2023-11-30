from enum import Enum

class CandyType(Enum):
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4

class Candy():
    def __init__(self, name, mass_in_grams, amount, price, type):
        self.__name = name
        self.__mass_in_grams = mass_in_grams
        self.__amount = amount
        self.__price = price
        self.__type = type
    
    def __str__(self):
        return f"{self.__name} - {self.__type} in the amount of {self.__amount}, weighing {self.__mass_in_grams} grams and costs {self.__price} UAH"
    
    def __repr__(self):
        return f"Name: {self.__name}; Mass: {self.__mass_in_grams}; Amount: {self.__amount}; Price: {self.__price}; {self.__type}"

    def ate(self):
        if self.__mass_in_grams * self.__amount > 2000:
            return "You're on a diet!"
        else:
            return "What delicious candies!"
    
    def get_name(self):
        return f'Name: {self.__name}'
    
    def get_amount(self):
        return f'Amount: {self.__amount}'
    
    def get_price(self):
        return f'Price: {self.__price}'
    
    def get_mass_in_grams(self):
        return f'Mass: {self.__mass_in_grams} grams'
    
    def get_type(self):
        return f'{self.__type}'

class Dinner():
    def __init__(self, day, time):
        self.__day = day
        self.__time = time
        self.candies = []
    
    def dinner_info(self):
        return f'It`s {self.__day} at {self.__time}:'

    def add_candy(self, __candy):
        self.candies.append(__candy)

    def add(self, __new_candies):
        self.candies.extend(__new_candies)
        
    def findTheMostExpensiveCandies(self):
        top_3 = sorted(self.candies, key = lambda x: x._Candy__price, reverse = True)
        return top_3[:3]
    
if __name__ == '__main__':
    candy1 = Candy("Snickers", 50, 3, 51, CandyType.BAR)
    candy2 = Candy("CornPop", 120, 2, 30, CandyType.POPCORN)
    candy3 = Candy("Pack of chocolate buttons", 400, 6, 360, CandyType.BUTTON)
    candy4 = Candy("Orbit", 10, 2, 10, CandyType.GUM)
    candy5 = Candy("Bounty", 50, 4, 48, CandyType.BAR)

    dinner1 = Dinner("Monday", "7:30 PM")
    """
    dinner1.add_candy(candy1)
    dinner1.add_candy(candy2)
    dinner1.add_candy(candy3)
    dinner1.add_candy(candy4)
    dinner1.add_candy(candy5)
    """
    dinner1.add([candy1, candy2, candy3, candy4, candy5])

    print(Dinner.dinner_info(dinner1))
    for candy in dinner1.candies:
        print(candy)
        print(Candy.ate(candy))

    print("-----"*20)

    print("Top 3 most expensive candies:")
    top_3 = dinner1.findTheMostExpensiveCandies()
    for i, candy in enumerate(top_3):
        print(f"{i+1}. {candy}")