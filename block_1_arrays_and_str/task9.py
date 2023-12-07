# 9. Write a program that replaces spaces in a string with a specific character.

txt = "Hello world! And you are welcome"

def replacer_spaces(txt, char):
    new_txt = ''
    for symbol in txt:
        if symbol == ' ':
            symbol = char
        new_txt += symbol
    return new_txt
    
new_txt = replacer_spaces(txt, "#")
print(new_txt)