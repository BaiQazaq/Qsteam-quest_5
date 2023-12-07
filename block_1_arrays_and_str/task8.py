# 8. Implement a method to count the number of vowels in a string.

vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]

def vowels_count(txt):
    cnt = 0
    for i in txt:
        if i in vowels:
            cnt += 1
    return cnt

txt = "Hello"

cnt = vowels_count(txt)
print(cnt)