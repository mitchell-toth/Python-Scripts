#Python code

def computeFibonacciNumber(n):
    if n==0: return 0
    if n==1: return 1
    return computeFibonacciNumber(n-2) + computeFibonacciNumber(n-1)

print(computeFibonacciNumber(10))
