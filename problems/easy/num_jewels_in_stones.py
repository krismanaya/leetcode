def numJewelsInStones(J: str, S: str) -> int:
    """
    You're given strings J representing the types of stones that are jewels, 
    and S representing the stones you have.  
    Each character in S is a type of stone you have.  
    You want to know how many of the stones you have are also jewels.
    The letters in J are guaranteed distinct, 
    and all characters in J and S are letters. 
    Letters are case sensitive, so "a" is considered a different type of stone 
    from "A".
    :type J: string
    :type S: string
    :rtype: int

    """
    return sum([S.count(j) for j in J if j in S])

assert numJewelsInStones(J='aA', S='aAAbbbbb') == 3 
