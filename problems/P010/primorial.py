n =int(input('enter your number :'))
n_p = 1
c=1
for x in range (2,n+1):
    c=1
    for y in range (2,x):
        if x % y == 0: 
            c=0
    if c == 1:
        n_p = n_p * x   
print(n_p) 