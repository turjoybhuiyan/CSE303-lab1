line = str(input("Enter a sentence: "))
sub = str("CSE303" "cse303")

l_str = len(line)
l_sub = len(sub)
c = 0
for i in range(0, l_str - l_sub + 1):
    if line[i:i + l_sub] == sub:
        c += 1

print(c )
