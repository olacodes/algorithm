# Given an unsorted list A, the maximum sum sub list is the sub list(contiguous elements) from A
# for which the sum of the elements is maximum. In this challenge, we want to find the sum of the maximum sum sub list.
# This problem is a tricky one because the list might have negative integers in any position,
# so we have to cater to those negative integers while choosing the continuous sublist
# with the largest positive values.

# Kadane's Algorithm
# * 0(n)
def find_max_sum_sublist(lst):
    cur_max = lst[0]
    global_max = lst[0]

    for i in range(1, len(lst)):
        if cur_max < 0:
            cur_max = lst[i]
        else:
            cur_max += lst[i]
        if cur_max > global_max:
            global_max = cur_max
    return global_max

lst = [-4,2,-5,1,2,3,6,-5,1]

print(find_max_sum_sublist(lst))
