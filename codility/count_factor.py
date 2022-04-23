# A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).
# Write a function: 
    # def solution(N)
# that, given a positive integer N, returns the number of its factors.
# For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

def count_factor(n):
    i = 1
    result = 0
    while(i * i < n):
        if (n % i == 0):
            result += 2
        i += 1
    if (i * i == n):
        result += 1
    return result

print(count_factor(1)) # O(log n)
