def binaryGap(n):
    ans = []
    count = 0
    binary_num = bin(n)[2:]

    for i in range(1, len(binary_num)):
        if binary_num[i] == '0':
            count += 1
        else:
            ans.append(count)
            count = 0
    if ans:
        return sorted(ans)[-1]
    else: 
        return 0
# print(bin(54)[2:])
print(binaryGap(54))