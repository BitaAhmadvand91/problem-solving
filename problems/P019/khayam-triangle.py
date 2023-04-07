n= int(input())
l=[1]
print(l)
l=[1,1]
print(l)
for x in range (1,n-1):
    new_l=[1,1]
    for y in range (0,x): 
        t=l[y] + l[y+1]
        new_l.insert(y+1,t)
    print(new_l)
    l=new_l