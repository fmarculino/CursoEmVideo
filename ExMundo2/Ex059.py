"""
Crie um programa que leia dois valores e mostre um menu como o ao lado
da tele:
Seu programa deveŕa realizar a operação solicitada em cada casoself.
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
"""
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
opcao = str('0')
while opcao != 5:
    print('[1] Soma')
    print('[2] Multiplica')
    print('[3] Maior')
    print('[4] Novo número')
    print('[5] Sair do programa')
    opcao = str(input('Digite sua opção: '))
    if opcao == str('1'):
        print(f'A soma do {valor1} + {valor2} = {valor1 + valor2}')
    elif opcao == str('2'):
        print(f'A multiplicação do {valor1} x {valor2} = {valor1 * valor2}')
    elif opcao == str('3'):
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'entre os valores digitados o maior valor é {maior}')
    elif opcao == str('4'):
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
    elif opcao == str('5'):
        break
    else:
        print('O valor digitado é invállido tente novamente.')
print('Fim do programa!')
