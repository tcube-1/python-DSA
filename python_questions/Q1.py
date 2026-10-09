user_input1 = [1,2,3,4,5,6]

# Q1 
user_input = input('enter input here: ').split(",")
nums = list(map(int,user_input))

print('Nums array',nums)
sum = 0
for i in nums:
  sum += i
print(f"sum of num: {sum}")
