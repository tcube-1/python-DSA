# tuple_user = tuple(input('enter and string with spaces: ').split())
# list_user = list(map(int, input('enter an intger with spaces: ').split()))

tuple_user = ("1","2","3")
list_user = [4,5,6] 

new_list=[] 
for i in range(len(tuple_user)):
  print(f"index: {i.__index__()}")
  for j in range(len(list_user)):
    print(i.__index__())


print(f"{new_list}")

names = ("Alice", "Bob", "tinku")
scores = [85, 90, 95]

for  (name, score) in zip(names, scores):
    print(f"Index: {name}{score}")