#factorial (5) -> 5 * 4 * 3 * 2 * 1 = 120

#number = 5
#result = 1
#for i in range (number) :
# result = result * (i+1)
# print ("iteration...")
# print (i)
# print (result)
#print ("And the grand final tally is")
#print (result)

#number = 5
#result = 1
#for i in range (number) :
# result = result * (i+1)
# print (result)
#print ("And the grand final tally is")
#print (result)

number = 65
result = 1
for i in range (number) :
 result = result * (i+1)
 print (i)
 print (result)
 if result > 10 ** 82:
  print ("Woah that's big")
print ("And the grand final tally is")
print (result)