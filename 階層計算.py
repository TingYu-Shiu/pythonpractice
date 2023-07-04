def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

print(factorial(6))


def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1)) #遞迴(不斷呼叫自己直到最底層)
    
print(fact(6))


import sys
sys.setrecursionlimit(4000) #遞迴次數預設為30000
print(sys.getrecursionlimit())