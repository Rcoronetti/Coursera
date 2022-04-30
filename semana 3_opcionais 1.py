x1= float(input("Digite o primeiro número da coordenada: "))
y1= float(input("Digite o segundo número da coordenada: "))
x2= float(input("Digite o terceiro número da coordenada: "))
y2= float(input("Digite o quarto número da coordenada: "))
import math
calculo= math.sqrt(((x1-x2)**2)+((y1-y2)**2))
if calculo>=10:
  print("longe")
else:
  print("perto")
