def solution(A):
    if len(A) == 1:
        return A[0]
        
    max_end = -100000
    max_slice = -1000000;

    for i in A:
        max_end = max(0+i, max_end + i)
        
        max_slice = max(max_end, max_slice)
        
    return max_slice
        

print(solution([-10, -2]))
print(solution([-2, 2]))
print(solution([3, 2, -6, 4, 0]))