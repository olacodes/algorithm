def solution(A):
    max_num = max(A)
    min_num = min(A)
    maxprofit = 0
   
    if A.index(min_num) < A.index(max_num):
        return min_num - max_num
    else:
        for i in range(len(A)):
            diff = max(A[i:]) - A[i]
            if diff > maxprofit:
                maxprofit = diff
        return maxprofit

print(solution([23171, 21011, 21123, 21366, 21013, 21367]))



