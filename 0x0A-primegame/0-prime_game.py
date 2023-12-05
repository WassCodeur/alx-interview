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
                return

def isWinner(x, nums):
    players = ["Ben", "Maria"]
    ben_nums = []
    maria_nums = []

    for i in range(x):
        temp = []
        for j in range(1, nums[i] + 1):
            temp.append(j)
        print(temp)
        for player in players:
            for z in range(len(temp)):
                try:
                    if isPrime(temp[z]):
                        if player == "Ben":
                            remove(temp[z], temp, ben_nums)
                        elif player == "Maria":
                            remove(temp[z], temp, maria_nums)
                except Exception:
                    pass
    return ben_nums, maria_nums
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    ben_nums, maria_nums = isWinner(x, nums)
    print(f"nums: {ben_nums}, del: {maria_nums}")
