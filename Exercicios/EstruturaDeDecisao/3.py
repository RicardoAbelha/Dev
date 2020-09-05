#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
#inf = str(input("qual seu sexo: "))
#f inf == "F":
#    print("Feminino")
#if else inf == "M":
#   print("Masculino")
#else:
#    print("Sexo Invalido")
    
sexo = str(input('Digite (F)-Feminino, (M)-Masculino: ').upper())
if sexo == 'M':
    print('Sexo Masculino.')
elif sexo == 'F':
    print('Sexo Feminino.')
else:
    print('Sexo Inválido.')