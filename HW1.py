#Exercise 0
def github() -> str:
    """
    This function returns a string that is the link to the github for this assignment
    """

    return "https://github.com/Julienmjohnson/Econ-481-HW-1/blob/main/HW1.py"

#Exercise 2
def evens_and_odds(x: int) -> dict:
    """
    This function takes a natural number n as an input and returns a dictionary where the key 'evens' is the sum of all even terms less than n and where the key 'odds' is the sum of all terms less than n
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
    This function takes two strings of dates in the format YYYY-MM-DD and another string with either the key word 'string' or 'float'. If the key word is 'float' it returns the number of days between the two dates. If the key word is 'string' it returns a string stating how many days are between the two dates.
    """
    dt1 = datetime.strptime(date_1, "%Y-%M-%d")
    dt2 = datetime.strptime(date_2, "%Y-%M-%d")
    delta = abs((dt1 - dt2).days)

    difference = {'float': delta, 'string': "There are " + str(delta) + " days between the two dates."}

    return difference[out]
    
#Exercise 4
def reverse(in_list: list) -> list:
    """
    This function takes a list and returns the same list with the elements ordered in reverse.
    """
    reversed = []
    for i in range(len(in_list)):
        reversed.append(in_list[-i-1])
    return reversed

#Exercise 5
def prob_k_heads(n: int, k: int) -> float:
    """
    The function takes two integers n and k where n is greater than or equal to k. It returns a float representing the probability of flipping a coin n times and having exactly k of them turn up heads.
    """
    numerator =1 
    denominator = 1
    for i in range(n-k+1, n+1):
        numerator *= i
    for i in range(1, k+1):
        numerator /= i
    for i in range(1, n+1):
        denominator *= 2
    
    return numerator/denominator