"""modules used in the code:"""
# enum module allows us to create enumeration types
from enum import Enum
# dataclass module provides a way to create data classes without the need to write methods
from dataclasses import dataclass


class CandyType(Enum):
    """Enumeration representing different types of candies

    This Enum class defines constants for various candy types, providing a readable and
    structured way to represent and work with different categories of candies
    """
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4


@dataclass
class Candy:
    """A class representing various candies

    Attributes:
        name (str): The name of the candy
        mass_in_grams (int): The mass of a single candy in grams
        amount (int): The amount of candies
        price (int): The price of a single candy in UAH
        typecandy (CandyType): The type of candy as an enumeration (BAR, BUTTON, POPCORN, GUM)
    """
    name: str
    mass_in_grams: int
    amount: int
    price: int
    type_candy: CandyType

    def __str__(self):
        return (
            f"{self.name} - {self.type_candy.name} in the amount of {self.amount},"
            f" weighing {self.mass_in_grams} grams and costs {self.price} UAH"
        )

    def __repr__(self):
        return (
            f"Name: {self.name}; Mass: {self.mass_in_grams};"
            f" Amount: {self.amount}; Price: {self.price}; {self.type_candy}"
        )

    def ate(self):
        """Check if consuming the specified quantity of candies exceeds a dietary limit

        This method evaluates whether the total mass of candies, considering both the
        quantity and individual mass, exceeds 2000 grams, indicating a potential dietary
        concern and returns result
        """
        if self.mass_in_grams * self.amount > 2000:
            return "You're on a diet!"
        return "What delicious candies!"

    def get_price(self):
        """getter for candy price | used in find_the_most_expensive_candies"""
        return f'Price: {self.price}'


class Dinner:
    """Class for Dinner part of the task"""
    def __init__(self, day, time):
        """Initialize a Dinner instance with the specified day and time

        Args:
            day (str): The day of the week for the dinner
            time (str): The time at which the dinner occurs
        """
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

    def find_the_most_expensive_candies(self):
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
    for i, candy in enumerate(dinner1.find_the_most_expensive_candies()):
        print(f"{i+1}. {candy}")
