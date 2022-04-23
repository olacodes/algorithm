# Find Intersection
# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
# Examples
# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1,4,13
# Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# Output: 1,9,10

def FindIntersection(strArr):
  '''
    split the list into two on string "";
    use set intersection to get what value in both list

  '''
  splitted_list = [i.split(', ') for i in strArr]
  first_list = set(splitted_list[0])
  second_list = set(splitted_list[1])

  union = list(first_list.intersection(second_list))
  if union == []:
    return False
  union.sort(key=int)
  union = ','.join(union)

  # code goes here
  return union

input = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
input1 = ["1, 2, 3, 4, 5", "6, 7, 8, 9, 10"]
# keep this function call here 
print(FindIntersection(input))
print(FindIntersection(input1))
