# Implement a function right_rotate(lst, k) which will rotate the given list by k. 
# This means that the right-most elements will appear at the left-most position in the list and so on. 
# You only have to rotate the list by one element at a time.
# * 0(1)
def rotate_right(lst, k):
        # Write your code here
    if k <= 0:
        return lst
    divisor = k % len(lst)
    left = lst[:-divisor]
    right = lst[-divisor:]
    return  right + left  

print(rotate_right([10,20,30,40,50], 3)) # [30,40,50,10,20]
print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
