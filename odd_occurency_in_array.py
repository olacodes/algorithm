
# The function should return the value of the unpaired element
def solution(A):
    # write your code in Python 3.6
    for item in A:
        count = A.count(item)
        if count % 2 != 0:
            return item

print(solution([9,9,3,3,2,7,7]))