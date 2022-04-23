# Write a function:
# def solution(A, B, K)
    # that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
    # { i : A ≤ i ≤ B, i mod K = 0 }
    
# For example, 
    # for A = 6, B = 11 and K = 2, your function should return 3, 
    # because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# SOLUTION 1 O(1) -- Constant Time
#  This solution use mathematics of dividing the upperbound and the lowerbound by the divisor and subtract upperbound result from lowerbound result
#  then check if lowerbound modulo divisor is 0 and add 1 to it and if not == 0 add 0 to it

def solution(A: int, B: int, K: int) -> int:
  '''
    Inputs:
      A - int: the lowerbound of number
      B - int: the upperbound of number
      K - int: number to be divisible by
    Outputs:
      Returns number of integer that are divisible by K between A and B
  '''
  return int(B // K - A // K + (1 if A % K == 0 else 0));


# SOLUTION 2 O(B-A)
# This solution loops through the number from the lowerbound to the upperbound and 
# check if number % divisor == 0 and return it length
def solution(A: int, B: int, K: int) -> int:
  result = [i for i in range(A, B+1) if i % K == 0]
  return len(result)

a, b, k= 6, 11, 2
print(solution(a, b, k))

