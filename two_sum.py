# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# Brute force approach (On2)
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
              if nums[i] + nums[j] == target:
                return [i, j]

        else:
          return []


# Better approach (On)
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