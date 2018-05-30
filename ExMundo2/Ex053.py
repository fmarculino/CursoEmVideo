"""
Crie um program que leia uma rase qualquer e diga se ela é um palíndromo,
desconsidenrando os espaços.
"""
# Tira os espaços antes e depois e já coloca a frase em maiusculo.
frase = str(input('Digite a frase: ')).strip().upper()
## frase = str('O lobo ama o bolo').strip().upper()
# Separa a frase em por palavras em uma lista
palavras = frase.split()
# Junta as palavras sem espaços
junto = ''.join(palavras)
## Modo tradicional de programação

# inverso = ''
# for letra in range(len(junto) -1, -1, -1):
#     inverso  += junto[letra]
##  Modo python de fazer essa parte do  codigo
inverso = junto[::-1] # Massa isso eu não sabia.

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
