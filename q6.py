a = int(input('Valor para A => '))
b = int(input('Valor para B => '))
c = int(input('Valor para C => '))

if a == b and b == c:
    print('IGUAIS')
elif a > b and a > c:
    print('O valor de A é o MAIOR.')
elif b > a and b > c:
    print('O Valor de B é o MAIOR.')
elif c > a and c > b:
    print('O valor de C é o MAIOR.')
elif (a == b or a == c) and b != c or (b == a or b == c) and a != c or (c == a or c == b) and a != b:
    print('Dois valores iguais e um diferente.')
else:
    print('Todos os valores diferentes.')