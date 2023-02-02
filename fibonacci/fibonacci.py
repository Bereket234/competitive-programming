def fibonacci(n):
    # visited= {}
    if n == 1:
        return 1
    if n == 0:
        return 0
    # if n-1 in visited:
    #     return visited[n-1]
    # if n-2 in visited:
    #     return visited[n-2]
    # visited[n-1]= fibonacci(n-1)
    # visited[n-2] = fibonacci(n-2)
    val= fibonacci(n-1) + fibonacci(n-2)
    print(val)
    return val
fibonacci(5)