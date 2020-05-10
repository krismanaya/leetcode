from typing import List
def replaceElements(arr: List[int]) -> List[int]:
    p0 = 0
    p1 = 1
    if len(arr) == 1:
        arr[0] = -1
    while p1 < len(arr):
        newArr = arr[p1: len(arr)]
        arr[p0] = max(newArr)
        p0 += 1
        p1 += 1
    arr[-1] = -1
    return arr