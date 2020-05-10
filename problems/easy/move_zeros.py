from typing import List
def moveZeroes(self, nums: List[int]) -> None:
    p0 = 0
    for p1, _ in enumerate(nums):
        if nums[p0] == nums[p1]:
            continue
        else:
            if nums[p0] != 0:
                p0 += 1
            else:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
    return nums
        