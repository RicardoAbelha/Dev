#aça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
valor = float (input("qual valor da sua hora: "))
horas = float (input("quantas horas vc trabalhou: "))
bruto = valor * horas
ir = (bruto * 0.11)
inss = (bruto * 0.08)
sind = (bruto * 0.05)
print("seu salrio Bruto: ", bruto)
print("pago para o IR:", ir)
print("pago para o inss: ", inss)
print("pago para o sindicato: ", sind)
print("seu salario liqueido é: ", bruto - ir - inss - sind)
