#!/usr/bin/python3
"""is the winner"""


def isPrime(n: int) -> bool:
    """check is the number is prime or not

    Arguments
    ---------
    n: int

    Return
    ------
    bool
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """is winner

    Arguments
    ---------
    x: int
    nums: list

    Return
    ------
    str
    """
    players = ["Maria", "Ben"]
    for i in nums:
        numbers = [j for j in range(1, i + 1)]
        for num in numbers:
            player = players[0]
            if (isPrime(num)):
                numbers.remove(num)
                for n in numbers:
                    if n % num == 0:
                        numbers.remove(n)

    return "Ben"
