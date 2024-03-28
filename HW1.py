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
