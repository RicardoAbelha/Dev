#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input("digite a primeiro numero: "))
num2 = int(input("digite a segundo numero: "))
num3 = int(input("digite a terceiro numero: "))


if num1 >= num2 and num1 >= num3 and num2 >= num3:
    print(f'A ordem decrescente é {num1} , {num2} e {num3}')
elif num1 >= num2 and num1 >= num3 and num3 >= num2:
    print(f'A ordem decrescente é {num1} , {num3} e {num2}')
elif num2 >= num1 and num2 >= num3 and num1 >= num3:
    print(f'A ordem decrescente é {num2} , {num1} e {num3}')
elif num2 >= num1 and num2 >= num3 and num3 >= num1:
    print(f'A ordem decrescente é {num2} , {num3} e {num1}')
elif num3 >= num1 and num3 >= num2 and num1 >= num2:
    print(f'A ordem decrescente é {num3} , {num1} e {num2}')
elif num3 >= num1 and num3 >= num2 and num3 >= num1:
    print(f'A ordem decrescente é {num3} , {num2} e {num1}')
