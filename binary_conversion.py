# binary_input = int(input("enter the digits: "))

# print(f"Your Digits is: {binary_input}")

class NumberConverter:
  def decimal_to_binary(self, decimal_number):
        ans = 0 
        place_value = 1
        while decimal_number > 0:
          remainder      = decimal_number % 2
          ans            = ans + (remainder * place_value)
          place_value    = place_value * 10
          decimal_number = decimal_number // 2
        return ans
  
  def binary_to_decimal(self, decimal_number):
        ans = 0 
        power = 1
        while decimal_number  > 0 :
          last_digit     = decimal_number % 10
          ans            = ans + (last_digit * power)
          power          = power * 2
          decimal_number = decimal_number // 10
        return ans
    

converter =  NumberConverter()
decimal_input = int(input("enter decimal here "))
binary_input = int(input("enter decimal here "))
print('decimal to binary', converter.decimal_to_binary(decimal_input)) 
print('decimal to binary', converter.binary_to_decimal(binary_input))
