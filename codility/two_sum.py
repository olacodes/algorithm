# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# Brute force approach O(n*2)
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
              if nums[i] + nums[j] == target:
                return [i, j]

        else:
          return []


# Better approach O(n)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for index, num in enumerate(nums):
            other = target - num
            
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index
                
        return []


my_solution = Solution()
print(my_solution.twoSum([2,11,15, 7, -2], 9))


# Best if array is already sorted O(log n)
# if array is not sorted O(n log n)
class Solution:
    @classmethod
    def find_two_sum(cls, arr, target):
        last = len(arr) - 1
        first = 0
        arr = sorted(arr) # O(n)

        while (first < last): # O(log n)
            if ((arr[first] + arr[last]) > target):
                last -= 1
            elif((arr[first] + arr[last]) < target):
                first += 1
            elif((arr[first] + arr[last]) == target):
                return True
        return False

print(Solution.find_two_sum([1,2,3,4], 8)) # O(n log n)