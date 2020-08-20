def fibo(n):
    return n if n <= 1 else (fibo(n-1) + fibo(n-2))

nums = [1,2,3,4,5,6]

[fibo(x) for x in nums]
# [1, 1, 2 ,3 ,5, 8]

[y for x in nums if (y:= fibo(x)) % 2 == 0]
# [2, 8]
