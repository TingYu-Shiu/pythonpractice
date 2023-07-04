def F(n):
    if n == 0 or n == 1:
        return n
    else:
        return F(n-1)+F(n-2)
    
print(F(10))


def fibonacciVal(n):
    memo = [None]*(n+1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    #print(memo)
    return memo[n]

print(fibonacciVal(500))


