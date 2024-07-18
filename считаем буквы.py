a = input()
b = 0
c = 0
d = len(a)
for i in a :
    if i =='c' or i == 'C' :
        b += 1
for j in a :
    if j == 'g' or j == 'G' :
        c += 1
print(((b + c) / d) * 100)