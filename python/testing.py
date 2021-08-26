def almostIncreasingSequence(sequence):
    sorted_sequence = sequence
    # sorted_sequence.sort()
    diff1 = sorted_sequence[1] - sorted_sequence[0]
    count = 0;
    for i in range(len(sorted_sequence)-1):
        diff = sorted_sequence[i + 1] <= sorted_sequence[i]
        if diff:
            count += 1
                      
        if count > 1:
            return False
            
    return True
    
arr = [1,2,1,2]
print(almostIncreasingSequence(arr))

a = [1,2,3,4]
a.pop(2)
print(a)