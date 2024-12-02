from typing import List

def p1(list1: List[int], list2: List[int]) -> int:
    res = 0
    for i in range(len(list1)):
        res+= abs(list1[i] - list2[i])
    return res

if __name__ == "__main__":
    list1 = []
    list2 = []
    with open("input.txt", "r") as f:
        for line in f:
            values = line.split()
            list1.append(int(values[0]))
            list2.append(int(values[1]))
    list1.sort()
    list2.sort()
    print(p1(list1, list2))
