#Faça um programa que pergunte o preço de três produtos
#  e informe qual produto você deve comprar,
#  sabendo que a decisão é sempre pelo mais barato.
prod1 = int(input("digite o valor do primeiro produto: "))
prod2 = int(input("digite o valor do segundo produto: "))
prod3 = int(input("digite o valor do  terceiro produto: "))
if prod1 < prod2 and prod2 < prod3:
    print("o primeiro é mais barato")
elif prod2 < prod3 and prod3 < prod1:
    print("o segundo é mais barato")
else:
    print("o terceiro é mais barato")