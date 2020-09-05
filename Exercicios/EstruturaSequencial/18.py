#Faça um programa que peça o tamanho de um arquivo para download (em MB)
#  e a velocidade de um link de Internet (em Mbps),
#  calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = int(input("Qual o tamanho do arquivo: "))
link = int(input("qual o link usado: "))
minutos = (tamanho / link)/ 60
print("o tempo de download sera de: ", round(minutos,2))