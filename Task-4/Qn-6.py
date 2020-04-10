def gen(s):
    for k in range(len(s), 0, -1):
        yield k

s = "Devanshi"
s1 = ""

for i in gen(s):
    s1 = s1+(s[i - 1])

print("Reverse string is : ", s1)