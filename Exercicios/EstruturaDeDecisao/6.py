#Faça um Programa que leia três números e mostre o maior deles.
num1 = int(input("digite a primeiro numero: "))
num2 = int(input("digite a segundo numero: "))
num3 = int(input("digite a terceiro numero: "))
if num1 > num2 and num2 > num3:
    print("o primeiro é maior")
elif num2 > num3 and num3 > num1:
    print("o segundo é maior")
else:
    print("o terceiro é maior")