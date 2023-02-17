n = int(input())
def prime_is (n): 
    c=0 
    for x in range (2, n):
        if n % x == 0 :
            c=1
            break
    if c==0:
        return True
prime_list=[]
if prime_is(n)== True:
   print(n) 
else:
    k=2
    r=n
    while k<=r :
       if prime_is(k)== True:
         while r%k==0:
                prime_list.append(k)
                r=r/k
                if r ==1:
                    print(prime_list)
                    break
       k= k +1
    

     
        
        