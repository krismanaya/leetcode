from typing import List

def sortArrayByParity(A: List[int]) -> List[int]:
    """
    Given an array A of non-negative integers, 
    return an array consisting of all the even elements of A, 
    followed by all the odd elements of A.
    """
    evenArray = list(filter(lambda x: x % 2 == 0, A))
    oddArray = list(filter(lambda x: x % 2 != 0, A))
    return evenArray + oddArray