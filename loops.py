array = []

for i in range(1,51):
  array.append(i)
  print("array started printing")

print(array)

for i in array:
  print(f"array started removing-> {{{i}}}")
  array.remove(i)
  print(f"array removed{array}")


print(array)