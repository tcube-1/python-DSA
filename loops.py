# array = []

# for i in range(1,51):
#   array.append(i)
#   print("array started printing")

# print(array)

# for i in array:
#   print(f"array started removing-> {{{i}}}")
#   array.remove(i)
#   print(f"array removed{array}")


# print(array)

arr = [10,22,3,4,5,6,7]
def findSmallestArray(arr):
  smallet = arr[0]
  smallest_index = 0
  for i in range(1,len(arr)):
    if arr[i] <smallet:
      smallet = arr[i]
      smallest_index = i
  return smallest_index

print(findSmallestArray(arr))

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallestArray(arr)
    newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort(arr))
