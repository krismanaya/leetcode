def numberOfSteps(num: int) -> int:
    
    """

    Given a non-negative integer num, return the number of steps to 
    reduce it to zero. 
    If the current number is even, you have to divide it by 2, 
    otherwise, you have to subtract 1 from it.
    :type n: int 
    :rtype: int

    """
    stepCounter = 0
    while num > 0:
        if num % 2 == 0:
            num = num//2
            stepCounter = stepCounter + 1
        else:
            num = num - 1
            stepCounter = stepCounter + 1
    return stepCounter


assert numberOfSteps(num=14) == 6
assert numberOfSteps(num=8) == 4