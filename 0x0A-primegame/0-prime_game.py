#!/usr/bin/python3
"""Prime Game"""


def isPrime(num: int) -> bool:
    """check if a number is prime

    Arguments
    ---------
    num: int

    Return
    ------
    bool
    """
    checker = False
    if num >= 2:
        numsqrt = int(num ** 0.5)
        if numsqrt <= 1:
            return True
        for i in range(2, numsqrt + 1):
            div = num / i
            if div % 1 != 0.0:
                checker = True
            else:
                return False

    return checker


def remove(choice: int, nums: list, deletes: list) -> list:
    if len(nums) != 0:
        for i in range(len(nums)):
            try:
                if nums[i] % choice == 0:
                    deletes.append(nums[i])
                    nums.pop(i)
            except Exception:
                return nums


def choice(player: str, nums: list, player_delete: list):
    """choice the player"""
    for i in nums:
        try:
            if isPrime(i):
                print(f"{player} before {nums}")
                remove(i, nums, player_delete)
                print(f"{player} after {nums}")
        except Exception:
            pass


def isWinner(x, nums):
    """is the winner

    Arguments
    ---------
    x: int
    nums: list

    Return
    ------
    None
    """
    players = ["Maria", "Ben"]
    ben_nums = []
    maria_nums = []

    for i in range(x):
        temp = []
        for j in range(1, nums[i] + 1):
            temp.append(j)
        print(temp)
        players = ["Maria", "Ben"]
        while (len(temp) != 1):
            if players[0] == "Maria":
                choice(players[0], temp, maria_nums)
                players[0] = "Ben"
                players[1] = "Maria"

            elif players[0] == "Ben":
                choice(players[0], temp, ben_nums)
                players[0] = "Maria"
                players[1] = "Ben"
            return "Ben"
