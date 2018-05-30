"""
A confederaçã nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INVFANTIL
- Até 19 anos: JUNIOR
- Até 24 anos: SENIOR
- Acima: MASTER
"""
from datetime import date

dtnascimento = int(input('Digite o ano de nascimento:'))
idade = date.today().year - dtnascimento

if 0 < idade <= 9:
    print(f'O atleta tem {idade} anos e é da categoria MIRIM')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} anos e é da categoria INFANTIL')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} anos e é da categoria JUNIOR')
elif 19 < idade <= 24:
    print(f'O atleta tem {idade} anos e é da categoria SENIOR')
else:
    print(f'O atleta tem {idade} anos e é da categoria MASTER')
