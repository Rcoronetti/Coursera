numero=int(input("Digite um número inteiro: "))
valor1= numero%3
valor2= numero%5
if valor1==0 and valor2==0:
  print("FizzBuzz")
else:
  print(numero)  
