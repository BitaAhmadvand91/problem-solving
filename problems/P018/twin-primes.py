n=int(input())
def prime_is (n): 
    c=0 
    for x in range (2, n):
        if n % x == 0 :
            c=1
            break
    if c==0:
        return True
a = []
for x in range(3,n-1):
    if prime_is (x):
        if prime_is (x+2):
            a.append((x,x+2))
for x in a:
    print(x)
    