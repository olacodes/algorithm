def product(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod

# * (0n)
def find_product(lst):
    # Write your code here
    if 0 not in lst:
        total_product = product(lst)
        return [total_product // i for i in lst]
    else:
        sorted_lst = sorted(lst)
        result = [0] * len(lst)
        if sorted_lst[0] == 0 and sorted_lst[1] == 0:
            return result
        index_zero = lst.index(0)
        lst.remove(0)
        total_product = product(lst)
        result[index_zero] = total_product
        return result


print(find_product([1, 2, 3, 4]))
print(find_product([4, 2, 1, 5, 0]))


# * (0n)
def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


# print(find_product([0, 1, 2, 3]))
print(find_product([1, 2, 3, 4]))
