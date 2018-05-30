"""
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
 e em quantos anos ele vai pagar.
 A prestação mensal, não pode exceder 30% do salário ou então o
 empréstimo será negado.
"""
valor = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o seu salário: R$ '))
anos = int(input('Em quantos anos você quer  pagar a casa: '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print(f'Para pagar uma casa de R$ {valor:.2f} em {anos} anos'
          f' a prestação será de R$ {prestacao:.2f}'
          f' Emprestimo pode ser CONCEDIDO')
else:
    print(f'Para pagar uma casa de R$ {valor:.2f} em {anos} anos'
          f' a prestação será de R$ {prestacao:.2f}'
          f' Emprestimo NEGADO')
