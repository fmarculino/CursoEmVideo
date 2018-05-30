salario = float(input('Qual é o salário do funcionário? R$ '))
novosal = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R$ {salario:.2f} com 15% de aumento,passa a '
      f'receber R$ {novosal:.2f}')
