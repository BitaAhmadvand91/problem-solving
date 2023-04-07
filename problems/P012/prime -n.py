n = int (input('enter nth prime number:'))
def prime_is (number):
    c= 0     
    for x in range (2, number):
        if number % x == 0 :
            c = 1
        if c==1: 
            break
    if c==0:
        return True
max=int(input('enter max :')) 
k=0
for i in range(2,max):
    if prime_is(i)==True:
        k=k+1
        if k==n:
            print(f'{i}')  
            break         
