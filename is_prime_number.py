def is_prime_number(n):
  '''
  Inputs:
    n -> int
  Output:
    returns True if n is a prime number and False if otherwise
  '''
  i = 2
  if n == 1:
    return True
  if n < 1:
    return False

  while(i * i <= n):
    if (n % i == 0):
      return False
    i += 1
  return True

print(is_prime_number(24)) # O(log n)