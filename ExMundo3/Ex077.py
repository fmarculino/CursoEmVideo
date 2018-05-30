"""
Crie um programa que tenha uma tupla com várias palavras (não
usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais.
"""
palavras = ('apreder', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for p in palavras:
    print(f'Na palavra {p} temos ', end='')
    for l in range(0, len(p)):
        if p[l] in 'aeiou':
            print(p[l], end=' ')
    print()
