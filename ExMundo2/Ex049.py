"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário
esolhe, só que agora utilizando um laço for.
"""
n = int(input('Digite um número: '))
print('-' * 12)
for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c:3}')
print('-' * 12)
