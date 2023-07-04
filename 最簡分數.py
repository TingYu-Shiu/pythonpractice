def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

m,n = input("輸入第一個分數的分子分母，中間以逗點做分隔:").split(',')
x,y = input("輸入第二個數字的分子分母，中間以逗點做分隔:").split(',')

m = int(m)
n = int(n)
x = int(x)
y = int(y)

result1 = ((m*y)+(x*n))/gcd(m*y+x*n,y*n)
result2 = (n*y)/ gcd(m*y+x*n,y*n)
print(m,"/",n,"+",x,"/",y,"=",round(result1),"/",round(result2))

    