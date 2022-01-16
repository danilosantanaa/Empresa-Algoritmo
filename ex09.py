precos = [
    {
        "codigo": "ABCD",
        "preco_unitario": 5.30
    },
    {
        "codigo": "XYPK",
        "preco_unitario": 6.0
    },
    {
        "codigo": "KLMP",
        "preco_unitario": 3.20
    },
     {
        "codigo": "QRST",
        "preco_unitario": 2.50
    }
]

# Mostrando os produtos
for chave, valor in enumerate(precos):
    print(f'Produto { chave + 1 }: ')
    print('*' * 20)
    for k, v in valor.items():
        print(f'{k} => {v}')
    print('~' * 30)

codigo = str(input('Codigo do produto: ')).strip().upper()

# Pesquisando o produto dado um codigo fornecido pelo usuário
pos_codigo = -1
pos = 0
while pos < len(precos): # O(N²)
    if precos[pos].get("codigo") == codigo:
        pos_codigo = pos
        break
    pos += 1

# Verificando se foi encontrado a posição do elemento, sendo pos_codigo diferente de -1
if pos_codigo != -1:

    quantidade = int(input('Digite a quantidade comprada: '))

    print('=' * 50)
    print(f'Codigo: { precos[pos_codigo].get("codigo") }')
    print(f'Preço Unitario: R${ precos[pos_codigo].get("preco_unitario") }')
    print(f'Comprando {quantidade} produtos, valor total é: R${ precos[pos_codigo].get("preco_unitario") * quantidade }')
else:
    print('<<< Codigo invalido! >>>')
