from typing import List

def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    s = ''
    for a in A:
        s += str(a)
    num = str(int(s) + K)
    L = []
    for chr in num:
        L.append(int(chr))
    return L