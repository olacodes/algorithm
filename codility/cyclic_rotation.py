# The solution function should rotate the array 
# cyclically with the (K) value given

def solution(A, K):
    
    array_length = len(A)
    if array_length == 0:
        return A
    
    divisor = K % array_length

    last_part = A[:-divisor]
    first_part = A[-divisor:]

    return first_part + last_part



print(solution([3,8,9,7,6],3))