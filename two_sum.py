

class Solution:
  def two_sum(self,nums:list[int],target:int)-> list[int]:
    num_map = {}
    for i, num in enumerate(nums):
      print(f"idx: {i}, target: {target} - num: {num}")
      value = target - num
      if value in num_map:
        return [num_map[value],i]
      print(f"value : {value}")
      num_map[num] =i 
    return []




nums = [1,2,4,9,10]

array1 = Solution()

result = array1.two_sum(nums,11)

print(f"answer is {result}")