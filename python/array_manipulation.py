a = [0] * 10

# b = a[1:5] * 3
# print(b)

b = a[0:5] = [3] * 4
c = a[1:2] = [4] * 6

print(b)
print(a)

from operator import add
def arrayManipulation(n, queries):
    A = [0] * n

    myArray = []
    for i in queries:
        A = [0] * n
        first = i[0] - 1
        second = i[1]
        third = i[2]
        c = A[first:second] = [third] * (second - first)
        myArray.append(A)

    # add_all = list(map(add, A, [i for i in myArray]))
    b = [j for i in myArray for j in i]

    return b

print(arrayManipulation(10, [[1,5,3],[4,5,6]]))

