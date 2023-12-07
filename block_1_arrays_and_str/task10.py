# 10. Find the smallest and largest strings in an array of strings.

txt = ["Al", "aL", "b", "W", "Zl", "hello"]
n = len(txt)
# min_txt = min(txt)
# max_txt = max(txt)
# print(min_txt, max_txt) #min_txt = "Al", max_txt = "hello"

def max_str(txt):
    max_sym = txt[0]
    for i in range(n):
        if max_sym < txt[i]:
            max_sym = txt[i]
    return max_sym

def min_str(txt):
    min_sym = txt[0]
    for i in range(n -1):
        if txt[i] < min_sym:
            min_sym = txt[i]
    return min_sym

x_lag = max_str(txt)
print(x_lag)

x_sml = min_str(txt)
print(x_sml)