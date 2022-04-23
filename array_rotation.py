def solution(A, K):
  '''
    Inputs:
      A - [] List of numbers to rotate
      K - int() Number of times to rotate the array
    Output:
      return [] -  list of rotated value of K times
      Example
        A = [3,8,9,7,6] 
        K =  3
        return  [9, 7, 6, 3, 8]
  '''

  length_A = len(A)
  # Return the same A [] list if the length of A is 0 or the same as K
  if K == length_A or length_A == 0:
    return A
  else:
    # Rotate the List [] in modulus of length of A [] and K
    num_rotate = K % length_A
    left_side = A[:-num_rotate]
    right_side = A[-num_rotate:]
    return right_side + left_side

test1, k1 = [3,8,9,7,6], 3 # [9, 7, 6, 3, 8]

print(solution(test1, k1)) 
