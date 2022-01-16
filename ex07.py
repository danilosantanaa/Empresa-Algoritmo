idade = int(input('Digite uma idade qualquer: '))

categoria = 'sem classificação'

if idade >= 5 and idade <= 7:
    categoria = 'infantil A'
elif idade >= 8 and idade <= 10:
    categoria = 'infantil B'
elif idade >= 11 and idade <= 13:
    categoria = 'juvenil A '
elif idade >= 14 and idade <= 17:
    categoria = 'juvenil B'
elif idade >= 18:
    categoria = 'adulto'
    
print('=' * 50)
print(f'STATUS CATEGORIA PARA {idade} ano(s): {categoria}')
