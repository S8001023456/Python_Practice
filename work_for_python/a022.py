palindrome = True
input_str = input()
for i in range(len(input_str)//2):
    if input_str[i] is not input_str[len(input_str) - 1 - i]:
        palindrome = False
if palindrome == True:
    print('yes')
else:
    print('no')
