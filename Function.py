def factorial(number):
  """this fonction computes the factorial"""
  result = 1
  for i in range(number):
   result = result * (i + 1)
  return result
  
print(factorial(6))
print(factorial(49))
print("The number of distinct 16/49 tickets:")
print(factorial(49) / (factorial(6) + factorial(49-6)))

def printy_sum(arg1, arg2):
 print(arg1)
 print(arg2)
 return arg1 + arg2
 
the_sum = printy_sum(3, 4)
print(the_sum)
