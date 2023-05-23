
n = int(input())
a = []
c = []
for x in range (0,n):
    b = int(input())
    a .append(b)
    w = int(input())
    c .append(w)
y = []
for x in range(0,n):
    s = a [x] + c[x]
    y .append(s) 
print(y)       