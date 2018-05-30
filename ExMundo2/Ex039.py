"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passoou do prazo.
"""
from datetime import date
anoatual = date.today().year
nascimento = int(input('Digite a data de nascimento:'))
idade = anoatual - nascimento
if idade > 18:
    print(f'Votem já tem {idade} e já passou {(anoatual - nascimento) - 18}')
    (f' do prazo para seu alistamento.')
    print(f'Seu alistamento deveria ter sido em ')
    (f'{anoatual - ((anoatual - nascimento) - 18)}')
elif idade == 18:
    print(f'Você tem {idade} e precisa se alistar agora.')
else:
    print(f'Você tem {idade} anos e faltão {18 - (anoatual - nascimento)}')
    (f') para se alistar')
    print(f'Seu alistamento será {anoatual + (18 - (anoatual - nascimento))}')
