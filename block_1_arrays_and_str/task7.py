# 7. Create a function that concatenates two strings into one.

txt1 = "Hello"
txt2 = "world"

def concanate(text1, text2):
    new_str = ""
    for l in text1:
        new_str += l
    for l in text2:
        new_str += l
    return new_str


text = concanate(txt1, txt2)
print(text)