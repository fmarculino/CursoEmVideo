"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valor lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.
"""
cont = maior = menor = total = 0
sn = str('S')
while sn == 'S':
    valor = int(input('Digite um valor: '))
    total += valor
    cont += 1
    if valor > maior:
        maior = valor
        if cont == 1:
            menor = valor
    elif valor < menor:
        menor = valor
    sn = str(input('Deseja continuar digitando S/N: ')).upper().strip()[0]
print(f'Ok, você digitou {cont} valores e a media dos valores é {total / cont}')
print(f'O MAIOR valor digitado foi {maior} e o MENOR foi {menor}\n')
print('FIM DO PROGRAMA')
