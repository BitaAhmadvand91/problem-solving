n_1=list(input('input first number: '))
n_2=list(input('input second number: '))
l_1=len(n_1)
l_2=len(n_2)
print(n_1)
print(n_2)
a=0
for x in range(1,l_2+1):
    d=0  
    for y in range (1,l_1+1):  
        c =int(n_2[l_2 - x ] )*int( n_1[l_1 -y])*(10**(y-1))
        d=d+c
    a=a+d*(10**(x-1))
print(a)
                        
    