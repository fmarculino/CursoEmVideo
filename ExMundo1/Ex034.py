""""
Escreva um programa que pergunte o salário de um funcionário  e
calcule o valor do seu aumento.
para salários superiores a R$ 1.250,00. calcule um aumento de 10%
para os inferiores ou iguais, o almento é de 15%
"""
salario = float(input('Qual o salário a calcular? '))
if salario > 1250:
    salrea = salario + salario * 10 / 100
    print(f'Seu salário atual é {salario:.2f} e terá um reajuste de 10% '
          f'seu novo salário é {salrea:.2f}')
else:
    salrea = salario + salario * 15 / 100
    print(f'Seu salário atual é {salario:.2f} e terá um reajuste de 15% '
          f'seu novo salário é {salrea:.2f}')
