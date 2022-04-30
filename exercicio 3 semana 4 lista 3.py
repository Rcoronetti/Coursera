numero=int(input("Digite um numero inteiro: "))
soma= 0
while numero >0:
  resto= numero%10
  numero= (numero-resto)//10
  soma=resto + soma
print (soma)    
