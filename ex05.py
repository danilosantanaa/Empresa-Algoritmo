nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = ( nota1 + nota2 + nota3 ) / 3

print(f'A média: {media}')
print('=' * 50)
if media >= 6:
    print('Aluno APROVADO!')
else:
    print('Aluno REPROVADO')
