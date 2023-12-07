# 5. Find the common elements between two arrays.

txt1 = ["TENT", "ROOT", "TOT", "LOOP", "ALA", "dala"]
txt2 = ["TENET", "ROT", "TOT", "LOP", "ALA"]
txt3 = []

for i in txt1:
    for j in txt2:
        if i == j:
            txt3.append(i)

print(txt3)