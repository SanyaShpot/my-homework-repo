"""modules for enum type and dataclass decorator"""
from enum import Enum
from dataclasses import dataclass


class CandyType(Enum):
    """Enum class for candy type"""
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4


@dataclass
class Candy:
    "Class for candies"
    name: str
    mass_in_grams: int
    amount: int
    price: int
    typecandy: CandyType

    def __str__(self):
        return (
            f"{self.name} - {self.typecandy} in the amount of {self.amount},"
            f" weighing {self.mass_in_grams} grams and costs {self.price} UAH"
        )

    def __repr__(self):
        return (
            f"Name: {self.name}; Mass: {self.mass_in_grams};"
            f" Amount: {self.amount}; Price: {self.price}; {self.typecandy}"
        )

    def ate(self):
        """Method for eating candy"""
        if self.mass_in_grams * self.amount > 2000:
            return "You're on a diet!"
        return "What delicious candies!"

    def get_price(self):
        """getter for candy price | used in findthemostexpensivecandies"""
        return f'Price: {self.price}'


class Dinner:
    """Class for Dinner part of the task"""
    def __init__(self, day, time):
        """init method for Diner class"""
        self.__day = day
        self.__time = time
        self.candies = []

    def dinner_info(self):
        """Returns information about dinner time and day of the week"""
        return f'It`s {self.__day} at {self.__time}:'

    def add_candy(self, __candy):
        """Add candy in candies list for dinner"""
        self.candies.append(__candy)

    def add_some_candies(self, __new_candies):
        """Add more than 1 candy"""
        self.candies.extend(__new_candies)

    def findthemostexpensivecandies(self):
        """Method for finding top 3 most expensive candies"""
        top_3_most_expensive = sorted(self.candies, key=lambda x: x.get_price(), reverse=True)
        return top_3_most_expensive[:3]


if __name__ == '__main__':
    candy1 = Candy("Snickers", 50, 3, 51, CandyType.BAR)
    candy2 = Candy("CornPop", 120, 2, 30, CandyType.POPCORN)
    candy3 = Candy("Pack of chocolate buttons", 400, 6, 360, CandyType.BUTTON)
    candy4 = Candy("Orbit", 10, 2, 10, CandyType.GUM)
    candy5 = Candy("Bounty", 50, 4, 48, CandyType.BAR)

    dinner1 = Dinner("Monday", "7:30 PM")
    dinner1.add_some_candies([candy1, candy2, candy3, candy4, candy5])

    print(Dinner.dinner_info(dinner1))
    for candy in dinner1.candies:
        print(candy)
        print(Candy.ate(candy))

    print("-----"*20)

    print("Top 3 most expensive candies:")
    top_3 = dinner1.findthemostexpensivecandies()
    for i, candy in enumerate(top_3):
        print(f"{i+1}. {candy}")
