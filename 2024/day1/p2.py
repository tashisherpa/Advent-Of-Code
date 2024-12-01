from typing import *

list1 = []
list2 = {}
with open("input.txt", "r") as f:
    for line in f:
        values = line.split()
        val1 = int(values[0])
        val2 = int(values[1])
        list1.append(val1)
        list2[val2] = list2.get(val2, 0) + 1

    
list1.sort()

def p2(list: List[int], list2: dict[int, int]) -> int:
    res = 0
    for num in list1:
        if num in list2:
            res += num * list2[num]
    return res

print(p2(list1, list2))