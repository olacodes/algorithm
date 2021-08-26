def minimumBribes(q):
    count = 0
    list_length = len(q)
    for i in range(list_length):
        if i + 1 < list_length:
            if q[i] > q[i + 1]:
                diff = q[i] - q[i + 1]
                
                if diff > 2:
                    print('Too chaotic')
                    return
                count += diff 
    print(count)
    return
# minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             # print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

a = {'password': ""}

print(a.get('passwords', 'fcgvhjbknl'))

b = a.get('username')

print(b)

print(len(''))



