random_str = input()
for word in random_str:
    print(chr(ord(word) - 7), end = "", sep = "")
print()
