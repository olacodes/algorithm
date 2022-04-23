import itertools
def solution(A: [], N: int) -> []:
  '''
    Inputs:
      A: [] - list of integers
      N: int - An integer representing the number of counter starting from 0
    Outputs:
      returns [] a list of integers representing the values of the counter
    Example:
      A = [3, 4, 4, 6, 1, 4, 4], N = 5
      return [3, 2, 2, 4, 2]
  '''

  if N > 100000 or len(A) <= 1:
    return A
  # result = list(itertools.repeat(0, N))
  result = [0] * N

  max_val = 0

  for i in range(len(A)):
    current_val = A[i]
    if current_val <= N:

      result[current_val - 1] = result[current_val - 1] + 1
      
      if result[current_val - 1] > max_val:
        max_val = result[current_val - 1]

    else:
      # result = list(itertools.repeat(max_val, N))
      result = [max_val] * N

  return result


test1, num1 = [3, 4, 4, 6, 1, 4, 4], 5 # [3, 2, 2, 4, 2]
print(solution(test1, num1))
