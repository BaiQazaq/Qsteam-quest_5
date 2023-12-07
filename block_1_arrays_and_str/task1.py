# 1. Write a program to find the maximum number in an array.

lst = [2, 4, 9, 4, 23, 45, 2, 12]
a = 0

for i in lst:
    if i > a:
        a = i
    else:
        continue
print(a)
