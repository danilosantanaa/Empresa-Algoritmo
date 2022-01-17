PESO1 = 2
PESO2 = 3
PESO3 = 5

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

mp = ( nota1 * PESO1 + nota2 * PESO2 + nota3 * PESO3 ) / ( PESO1 + PESO2 + PESO3 )

print(f'A média ponderada das notas {nota1} {nota2} e {nota1} é {mp} ')