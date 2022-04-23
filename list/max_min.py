# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list
# such that the 0th index will have the largest number, the 1st index will have the smallest,
# and the 2nd index will have second-largest, and so on. In other words,
# all the even-numbered indices will have the largest numbers in the list in descending order
# and the odd-numbered indices will have the smallest numbers in ascending order.


# * 0(nlogn)
def max_min(lst):
    if len(lst) < 2:
        return lst
    lst.sort()
    result = []
    first_index = 0
    last_index = len(lst) - 1
    while first_index != last_index and first_index < last_index:
        result.extend((lst[last_index], lst[first_index]))
        first_index += 1
        last_index -= 1

    if len(result) != len(lst):
        result.append(lst[first_index])

    return result


# lst = [1, 2, 3, 4, 5]
# print(max_min(lst))
print(max_min([1, 2, 3, 4, 5, 6, 7]))  # [7, 1, 6, 2, 5, 3, 4]
print(max_min([-10, -1, 1, 1, 1, 1]))  # [1, -10, 1, -1, 1, 1]
