"""
Problem: Calculate factorial of a given integer through recursion and implement the function using threading.

Solution overview: We handle base case n = 0,1 and implement the recursion. 

Notes: Since in our case, there are no instances executing parallely, need to understand why threading is relevant here.

"""

def fact(n):
    if (n == 0) or (n == 1):
        return 1

    else:
        return (n * fact(n-1))


print(fact(4))