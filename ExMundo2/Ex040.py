"""
Crie um programa que leia duas notas de um alno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média  atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Parabéns sua média foi {media} e você está APROVADO')
elif 7 > media >= 5:
    print(f'Sua média foi {media} e você esta de RECUPERAÇÃO')
else:
    print(f'Sua média foi {media} e você foi REPROVADO.')
