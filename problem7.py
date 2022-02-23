def Sum(List):
    total = 0
    for j in range(Number):
        total = total + List[j]
    return total
List = []
Number = int(input("Number of list : "))
for i in range(1, Number + 1):
    value = int(input("Value %i : " %i))
    List.append(value)
total = Sum(List)
print("\n Total : ", total)