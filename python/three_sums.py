class Solution:
  def three_sums(self,arr):
    result = []
    array_length = len(arr)
    for i in range(array_length):
      first = arr[i]
      for j in range(i+1, array_length):
        second = arr[j]
        for k in range(j+1, array_length):
          third = arr[k]
          if first + second + third == 0:
            result.append([first, second, third])
            break;
    return result

nums = [-1, 0, 1, 2, -1, -4]

three_sums = Solution()
print(three_sums.three_sums(nums))
            
