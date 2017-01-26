
def fib(n):
    if n in (0, 1):
        return 1
    if n & 1:
        return fib((n+1)//2 - 1) * (2*fib((n+1)//2) - fib((n+1)//2 - 1))
    a, b = fib(n//2 - 1), fib(n//2)
    return a*a + b*b

K = int(input())

if K > 2:
    print(fib(K-2), fib(K-1))
elif K == 2:
    print('1 1')
elif K == 1:
    print('0 1')
else:
    print('1 0')
