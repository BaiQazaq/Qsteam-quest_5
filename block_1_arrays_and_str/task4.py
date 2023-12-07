# 4. Write a method to check if a string is a palindrome.

txt = ["TENET", "ROOT", "TOT", "LOOP", "ALA"]
palindrome = []

cnt = 0
for i in txt:
    a = []
    for l in i:
        a.insert(0, l)
    b = "".join(a)
    if i == b:
        palindrome.append(i)
    cnt += 1

print(palindrome, cnt)