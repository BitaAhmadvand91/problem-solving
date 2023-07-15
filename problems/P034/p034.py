n = input()
print(n)
def prime_is (number):
    c= 0     
    for x in range (2, number):
        if number % x == 0 :
            c = 1
        if c==1: 
            break
    if c==0:
        return True
max=len(n)
for y in range (0,max):
    for x in range (y+1,max+1):
        w = n[y:x]
        r=int(w)
        if prime_is (r)== True:
            print(r)

    
