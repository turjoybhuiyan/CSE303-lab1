def even_sum(List):
    Even_Sum = 0
    for j in range(Number):
        if(List[j] % 2 == 0):
            Even_Sum = Even_Sum + List[j]
    return Even_Sum
List = []
Number = int(input("Number of list: "))
for i in range(1, Number + 1):
    value = int(input("Value %d: " %i))
    List.append(value)
Even_Sum = even_sum(List)
print("\n Total =  ", Even_Sum)

given_string = input('Enter a string: ')

even_chars = []
odd_chars = []

for i in range(len(given_string)):
    if i % 2 == 0:
        even_chars.append(given_string[i])
    else:
        odd_chars.append(given_string[i])

print('Odd characters: {}'.format(odd_chars))
print('Even characters: {}'.format(even_chars))
