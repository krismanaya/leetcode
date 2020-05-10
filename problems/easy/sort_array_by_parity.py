from typing import List

def sortArrayByParity(A: List[int]) -> List[int]:
    """
    Given an array A of non-negative integers, 
    return an array consisting of all the even elements of A, 
    followed by all the odd elements of A.
    """
    p0 = 0
    for p1, _ in enumerate(A):
        if A[p0] % 2 != 0 and A[p1] % 2 != 0:
            continue
        else:
            A[p0], A[p1] = A[p1], A[p0]
            p0 += 1
    return A