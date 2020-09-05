#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: (72.7*altura) - 58
alt = float (input("qual sua altura: "))
pesoIde = (72.7 * alt)-58
print("Seu peso ideal é: ", pesoIde)

peso = float (input("qual seu peso atual: "))
print("é precisoa perder: ", peso - pesoIde)