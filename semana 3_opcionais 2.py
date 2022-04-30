a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))
delta= (b**2)-(4*a*c)
import math
raizdelta= math.sqrt(delta)
if delta > 0:
  x1= (-(b)+raizdelta)/(2*a)
  x2= (-(b)-raizdelta)/(2*a)
  if x1<x2:
     print("as raízes da equação são",x1,"e",x2)
  else:
     print("as raízes da equação são",x2,"e",x1)
elif delta ==0:
  x=(-(b)+raizdelta)/(2*a)
  print("a raiz desta equação é x",x)
else:
  print("esta equação não possui raízes reais")
