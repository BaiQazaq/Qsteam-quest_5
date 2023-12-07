# 6. Write a program to sort an array of integers in ascending order.

array = [2, 4, 9, 4, 23, 45, 2, 12]
cnt = 0
n = len(array)

for run in range(n-1):
    for j in range(n-1):
        if array[j] > array[j + 1]:
           cnt += 1
           array[j], array[j + 1] = array[j + 1], array[j]

print(cnt)
print(array)