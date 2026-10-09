nums_input = [1,2,3,4,5,6,7]
nums_input1 = [10,-10,2,5,6,7,0,1]
nums_input2 = [1,2,3,5,9]

nums = list(map(int, nums_input2))
odd_list = []
for i in nums:
  if i % 2 !=0:
    val = i*i 
    odd_list.append(val)


print(odd_list)


odd_list1 = [i* i for i in nums_input  if i % 2 !=0]
print(odd_list1)