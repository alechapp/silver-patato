w = 8
Height= 4
c = "+"
#Top = Corner,'-'* width,Corner
#Side = "|",' '* width,"|"
#print (Top)
#print (Side)

t= "-"
for i in range(w - 2):
 t = c + "-"
t = t + c
#Top = Corner + border + Corner
print (t)
