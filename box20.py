height = 10
width = 10
for j in range(height - 2):
  side = "|"
  for i in range(width - 2):
    if (i - j) % 3 == 0:
      side = side + "\\"
    else:
      side = side + " "
  side = side + "|"    
  print(side)

#height = 10
#width = 10
#for j in range(height - 2):
# side = "|"
# for i in range(width - 2):
#  side = side + " "
# side = side + "|"
#print(side)

# if i % 3 == 0: