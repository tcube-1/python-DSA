

class Solution:
  def two_sum(self,nums:list[int],target:int)-> list[int]:
    num_map = {}
    for i, num in enumerate(nums):
      req = target - num 
      if req in num_map:
        return [num_map[req],i]
      num_map[num] = i
      
      print(f"\n req =>{req}<=\n")
      print(f"idx: {i}, target: {target}-{num} and array:  {nums}")
    return []


nums = [1,2,4,9,10]

array1 = Solution()

result = array1.two_sum(nums,11)

print(f"answer is {result}")