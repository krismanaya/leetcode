from typing import List
def removeDuplicates(nums: List[int]) -> int:
    p0 = 0
    for p1, _ in enumerate(nums):
        if nums[p0] == nums[p1]:
            # nothing too do here
            continue
        else:
            p0 += 1
            nums[p0] = nums[p1]
    return nums[0: p0 + 1]
    