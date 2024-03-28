#Exercise 0
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/Julienmjohnson/Econ-481-HW-1/blob/main/HW1.py"

#Exercise 2
def evens_and_odds(x: int) -> dict:
    """
    this function takes a natural number n as an input and returns a dictionary where the key 'evens' is the sum of all even terms less than n and where the key 'odds' is the sum of all terms less than n
    """
    evens = 0
    odds = 0
    i = 0
    while (i < x):
        evens += i
        i += 2
    i = 1
    while (i < x):
        odds += i
        i += 2
        
    return {'evens':evens, 'odds':odds}

#Exercise 3
from typing import Union
from datetime import datetime, date, time, timedelta

def time_diff(date_1: str, date_2: str, out: str='float') -> Union[str,float]:
    """
    This function takes two strings of dates in the format YYYY-MM-DD and another string with either the key word 'string' or 'float'. 
    If the key word is 'float' it returns the number of days between the two dates. If the key word is 'string' it returns a string stating how many days are between the two dates.
    """
    dt1 = datetime.strptime(date_1, "%Y-%m-%d")
    dt2 = datetime.strptime(date_2, "%Y-%m-%d")
    delta = abs((dt1 - dt2).days)

    difference = {'float': delta, 'string': "There are " + str(delta) + " days between the two dates."}

    return difference[out]
    
#Exercise 4
def reverse(in_list: list) -> list:
    """
    This function takes a list and returned a list with the elements ordered in reverse.
    """
    reversed = []
    for i in range(len(in_list)):
        reversed.append(in_list[-i-1])
    return reversed

