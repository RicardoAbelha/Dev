valor = int(input('Entre com o valor: '))
inicio = 1
print(inicio)
print(valor)
while inicio < valor:
    if (inicio%2 ==0):
        print(inicio, "valor é par")
        inicio = inicio + 1
    else:
        print(inicio, "valor é inpar")
        inicio = inicio + 1


