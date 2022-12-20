"""
Problem: Find all possible sets of consequetive odd numbers such that the sum of each set is equal to the given number i.e., X.

Solution overview: We find ranges that satisfy the following constraint: S(i,j) such that j^2 - i^2 = Req_sum

"""


def calcSet(n):
    count = 0
    sum = 0
    i = 0
    j = 1
    while (i<(n+1)/2):
        sum = (j+i)*(j-i)
        if sum < n:
            j += 1
            #print(i,j,count)

        elif sum > n:
            i += 1
            #print(i,j,count)

        else:
            i += 1
            count += 1
            #print(i,j,count)

    return count

x = int(input("Enter total number of candies: "))

print(calcSet(x))