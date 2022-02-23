def pallindrome_checker_151(line):
    line = line.lower()
    if line == line[::-1]:
        return 1


line = str(input("Enter a word: "))

if pallindrome_checker_151(line) == 1:
    print(line, "is a pallindrome word")
else:
    print(line, "is not a pallindrome word")