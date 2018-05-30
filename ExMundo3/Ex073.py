"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol. na ordem de colocação. Depois
mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da chapecoense.
"""
brasileirao = ('Atlétio', 'Flamento', 'Corinthians', 'Palmeiras',
               'Fluminense', 'América-MG', 'São Paulo', 'Grêmio',
               'Vasco da Gama', 'Botafogo', 'Sport Recife', 'Cruzeiro',
               'EC Vitória', 'Santos', 'Chapecoense', 'Atlético-PR',
               'Internacional', 'Bahia', 'Ceará SC', 'Paraná')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=' * 20)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabéticas: {sorted(brasileirao)}')
print('-=' * 20)
print(f'A chapecoense está na {brasileirao.index("Chapecoense") + 1}º posição')
# Outra forma de fazer
for id, time in enumerate(brasileirao):
    if time == "Chapecoense":
        print(f'O {time} está na {id + 1}º posição')
