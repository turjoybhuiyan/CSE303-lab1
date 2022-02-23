def even_sum(List):
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    List.append(value)

smallest = largest = List = []

for j in range(1, Number):
    if(smallest > List[j]):
        smallest = List[j]
    if(largest < List[j]):
        largest = List[j]

print("The Smallest Element in this List is : ", smallest)
print("The Largest Element in this List is : ", largest)