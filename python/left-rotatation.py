def rotLeft(a, d):
    lenght_arr = len(a)
    divisor = d % lenght_arr

    first_part = a[:divisor]
    second_part = a[divisor:]

    return second_part + first_part

    