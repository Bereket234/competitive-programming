def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
def fact(n):
    res=1
    for i in range(n, 0,-1):
        res*= i
    return res
print(factorial(5))
print(fact(5))