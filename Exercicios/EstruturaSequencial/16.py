#Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
#  que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#  Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = float (input("qual a area a ser pintada: "))
cober = area /3
litros = cober / 18
valor = litros * 80
print("sera usado: ", litros, "latas")
print("Valor total: ", valor) 