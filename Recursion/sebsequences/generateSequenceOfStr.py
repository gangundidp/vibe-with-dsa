from typing import *

# Power Set

def generateSequenceOfString(s: str):
    n = len(s)
    total = 1<<n
    res = []
    
    for i in range(total):
        sub_sequence = []
        for j in range(n):
            if i & (1<<j):
                sub_sequence.append(s[j])
        res.append("".join(sub_sequence))
            
    return res

# print("Output: ", generateSequenceOfString("abc"))


def recursiveGenerateSubseqString(s: str, idx: int, curr: List, res: List):
    if idx == len(s):
        res.append("".join(curr))
        return
    
    recursiveGenerateSubseqString(s, idx+1, curr, res)
    
    curr.append(s[idx])
    recursiveGenerateSubseqString(s, idx+1, curr, res)
    
    curr.pop()
    
if __name__ == "__main__":
    res = []
    curr = []
    
    s = input("s: ")
    
    recursiveGenerateSubseqString(s, 0, curr, res)
    
    print("Output: ", res)