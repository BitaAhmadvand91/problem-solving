n = int(input())
b = 0
if n < 1000 :
    for x in range (1,n+1):
        b = b + x
    print (b) 
else:
    print(f'nuamber is more than 1000')  