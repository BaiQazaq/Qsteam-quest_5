# 2. Create a function to calculate the average of the numbers in an array.

lst = [2, 4, 9, 4, 23, 45, 2, 12]
a = 0
cnt = 0
for i in lst:
    a += i
    cnt += 1

print(a, cnt)
print(a / cnt)
