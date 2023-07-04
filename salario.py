valor = int(input("Digite o valor do seu emprestimo"))
cal1 = valor + (4/100*valor)
cal2 = valor + (11/100*valor)
par1 = (cal1/24)
par2 = (cal2/24)
if valor >= 250000:
    print("O valor do emprestimo é {0}, e você vai pagar no total{1}".format(valor,cal1))
    print("O numero de parcelas sera 24 entao pagara por mes: {}".format(par1))
casa = float(input("Digite o Valor da Casa : R$"))
salario = float(input("Digite o seu salario: R$"))
ano = int(input("Quantos anos você vai pagar :"))
prestacao = casa / (ano*12)
print("O valor pago em uma casa de :{:.2f} em {} anos".format(casa ,  ano))
print("A prestação é de {:.2f}".format(prestacao))
if prestacao >= (50/100)*salario:
    print("Emprestimo Negado")
else:
    print("Emprestimo aprovado") 