

def alphabets(n:int) -> list[str]:
  ascii = ord('0')
  result = []
  for i in range(n):
    char = chr(ascii + i)
    result.append(f'{i+1}:{char}')
  print(f"total alphabets:{len(result)}")
  return result

letters = alphabets(262)
print("Alphabets", letters)

