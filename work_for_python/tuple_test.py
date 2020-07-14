a,b = [1, 2, 3], [4, 2, 1]
t = (a, b)  # call by address
print(a)
print(t)
a[0] = 2
print(a)
print(t)
