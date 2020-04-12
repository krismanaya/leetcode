from typing import List

def singleNumber(self, nums: List[int]) -> int:
    """
    Given a non-empty array of integers, 
    every element appears twice except for one. Find that single one.

    """
    for n in nums:
        if nums.count(n) == 1:
            return n
        else:
            continue