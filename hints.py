import numpy as np


def fib_recur(n):
    if (n <= 2):
        return 1
    return fib_recur(n-1) + fib_recur(n-2)

def fib_dp(n, trav):
    if(n in trav):
        return trav[n]
    if (n <= 2):
        return 1
    trav[n] = fib_dp(n - 1, trav) + fib_dp(n - 2, trav)
    return trav[n]

trav = np.array()
print(fib_dp(50, trav))