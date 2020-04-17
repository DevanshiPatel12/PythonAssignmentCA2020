# Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

x=[1,2,3,4,5,6,7,8,9,-1]
s = set()
n = set()
for i in x:
    for j in x:
        sum = i + j
        if sum == 8:
            if i not in s and j not in s:
                s.add(i)
                s.add(j)
                n.add((i,j))
print(n)