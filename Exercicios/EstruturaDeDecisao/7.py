#Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input("digite a primeiro numero: "))
num2 = int(input("digite a segundo numero: "))
num3 = int(input("digite a terceiro numero: "))

# Achando o maior número
maior = num1

if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3

print('Maior: ',maior)

    # Achando o menor número
menor = num1

if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3

print('Menor: ',menor)

