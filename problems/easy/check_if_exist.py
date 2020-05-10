from typing import List
def checkIfExist(arr: List[int]) -> bool:
    for index1 in range(len(arr)):
        for index2 in range(len(arr)):
            if index1 != index2:
                if arr[index1] == 2*arr[index2]:
                    return True
    return False