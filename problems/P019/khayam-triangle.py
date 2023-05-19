n= int(input())
l=[1]
print(l)
l=[1,1]
print(l)
for x in range (1,n-1):
    l=[1,1]
    for y in range (0,x-1):
        t=l[y] + l[y+1]
        l.insert(y+1,t)
    print(l)