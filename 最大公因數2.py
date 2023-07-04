x = int(input("please input a number:"))
y = int(input("please input a number:"))

z = list()

def gcd(n,n1):
    if x > y :
        c = x
    else:
        c = y
    for k in range(c, 2, -1):
        if x % k == 0 and y % k == 0:
           z.append(k)
 
       
result = gcd(x,y)
       
        
print(x,"與",y,"的最大公因數為:",result)



