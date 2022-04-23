# This is a demo task.
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.



def solution(A):
  '''
    Inputs:
      A - List of Numbers
    Outputs:
      integer - Returns the smallest positive integer(greater than zero) that does not occur in A
  '''

  # sort the list
  A.sort(key=int)

  # Check if the first element is less than or equal 1 and if 1 it's not in the list (A)
  if A[0] <= 1:
    if 1 not in A:
      return 1
    else:
      # find index of the first occurrence of 1
      index_of_one = A.index(1)

      # reduce the list from the first occurrence of 1 to the end
      remaining_list = list(set(A[index_of_one:]))

      # Sort the list using int as key
      remaining_list.sort(key=int)

      # get index of all remaining list 
      list_index = [i+1 for i in range(len(remaining_list))]

      # Using set data structure to get the difference between the list index and remaining list
      ans = list(set(list_index) - set(remaining_list))

      # If there is no difference return the last item + 1
      if ans == []:
        return remaining_list[len(remaining_list) - 1] + 1
      else:
        ans.sort(key=int)
        return ans[0]
  else:
    return 1

test1 = [1, 3, 6, 4, 1, 2] # 5
test2 = [1, 2, 3] # 4
test3 = [-1, -3] # 1
print(solution(test1))
print(solution(test2))
print(solution(test3))

