l1=[1,2,3,4,1,2,3,4]

s=set()

for i in l1:
    if i not in s:
        s.add(i)

print(s)


