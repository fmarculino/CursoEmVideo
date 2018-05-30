"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoasself.
No final do programa, mostre:
- A média deidade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
"""
totidade = float(0)
nomemaisvelho = ''
idademaisvelho = int(0)
quantmulheres = int(0)
for c in range(1, 5):
    print(f'----- {c}º PESSOA -----')
    nome = input(f'Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo M/F: ').strip().upper()
    totidade += idade
    if idade > idademaisvelho and sexo == 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade < 20 and sexo == 'F':
        quantmulheres += 1
print(f'A média de idade do grupo é de {totidade / 4:.2f} anos.')
print(f'O nome do home mais velho tem {idademaisvelho}'
      f' e se chama {nomemaisvelho}')
print(f'No grupo tem {quantmulheres} mulheres com menos de 20 anos')
