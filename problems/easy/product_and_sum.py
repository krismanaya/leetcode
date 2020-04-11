


def subtractProductAndSum(n: int) -> int:
    import functools 
    """
    Given an integer number n, 
    return the difference between the product 
    of its digits and the sum of its digits.
    example:
    int = 123
    product = 1*2*3
    sum = 1+2+3
    result = product - sum
    :type n: int 
    :rtype: int
    """
    intArray = list(map(lambda x: int(x), str(n)))
    sumArray = functools.reduce(lambda a,b: a+b, intArray)
    prodArray = functools.reduce(lambda a,b: a*b, intArray)
    return prodArray-sumArray

assert subtractProductAndSum(234) == 15


    
