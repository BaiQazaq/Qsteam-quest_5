# 2. Implement a function to compare two strings without using built-in string comparison methods

def compare_str(str1, str2):
    dif = []
    com = []
    lst1 = list(str1)
    lst2 = list(str2)
    set1 = set(lst1)
    set2 = set(lst2)
    print(set1)
    print(set2)
    for i in set1:
        if i in set2:
            com.append(i)
        elif i not in set2:
            dif.append(i)
    for i in set2:
        if i in set1 and i not in com:
            com.append(i)
        elif i not in dif and i not in set1:
            dif.append(i)
    return dif, com

str1 = "Hello world"
str2 = "World beatiful"

dif, com = compare_str(str1, str2)
print(f"different symbols -> {dif}, common symbols -> {com}")