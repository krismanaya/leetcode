from typing import List

def findNumbers(nums: List[int]) -> int:
    """
    Given an array nums of integers, 
    return how many of them contain an even number of digits. 
    type: list
    rtype: int

    """
    return len(list(filter(lambda x: len(str(x)) % 2 == 0, nums)))


