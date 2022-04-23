# ------------------------------------------>
#  * SOLUTION 1 (On2)
# ------------------------------------------>

def find_sum(lst, k):
    for num in lst:
        new_lst = lst.copy()
        sec_num = 0
        sec_num = k - num if k >= num else num - k
        new_lst.remove(num)
        if sec_num in new_lst:
            return [num, sec_num]


print(find_sum([1, 3, 14, 5, 21, 60, 7, 6], 81))
print(find_sum([1, 2, 3, 4], 5))



# ------------------------------------------>
# * SOLUTION 2 (0nlogn)
# ------------------------------------------>
def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        elif item < a[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return index if found else -1


def find_sum(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k - lst[j])
        if index != -1 and index is not j:
            return [lst[j], k - lst[j]]


print(find_sum([1, 5, 3], 2))
print(find_sum([1, 2, 3, 4], 5))

# ------------------------------------------>
#  * SOLUTION 3 (0nlogn)
# ------------------------------------------>


def find_sum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.extend((lst[index1], lst[index2]))
            return result
    return False


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))
print(find_sum([1, 3, 14, 5, 21, 60, 7, 6], 81))


# SOLUTION 4 (0n)

def findSum(lst, value):
    foundValues = set()
    for ele in lst:
        if value - ele in foundValues:
            return [value-ele, ele]
        foundValues.add(ele)
    return False


print(findSum([1, 2, 3, 4], 6))
