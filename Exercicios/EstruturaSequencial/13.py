#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
alt = float (input("qual sua altura: "))
opcao = input("H ou M:")
if opcao == "H":
    print("seu peso ideal é: ", (72.7 * alt) - 58)
else:
    print("seu peso ideal é: ", (62.1 * alt) - 44.7)