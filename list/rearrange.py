# Implement a function rearrange(lst) which rearranges the elements such that all the 
# negative elements appear on the left and positive elements appear at the right of the list. 
# Note that it is not necessary to maintain the sorted order of the input list.

# * 0(n)
def rearrange(lst):
    neg = []
    pos = []
    # make a list of negative and positive numbers
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    # merge two lists and return
    return neg + pos

print(rearrange([10, -1, 20, 4, 5, -9, -6]))

# * 0(n) --> Time complexity
# * 0(n)
def rearrange(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr != leftMostPosEle:
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


print(rearrange([10, -1, 20, 4, 5, -9, -6]))
