def sec_largest(num_list):
   return new_list[-2]

num_list = [20, 50, 60, 70, 15, 17]
new_list = []

while num_list:
    min = num_list[0]
    for x in num_list:
        if x < min:
            min = x
    new_list.append(min)
    num_list.remove(min)

print("2nd Largest number :",sec_largest(num_list))