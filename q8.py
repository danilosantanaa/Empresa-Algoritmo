produtos = [
    {
        'especificacao': 'Cachorro quente',
        'codigo': 100,
        'preço': 1.20
    },

    {
        'especificacao': 'Bauru simples',
        'codigo': 101,
        'preço': 1.30
    },

    {
        'especificacao': 'Bauru com ovo',
        'codigo': 102,
        'preço': 1.50
    },

    {
        'especificacao': 'Hambúrger',
        'codigo': 103,
        'preço': 1.20
    },

    {
        'especificacao': 'Cheeseburguer',
        'codigo': 104,
        'preço': 1.30
    },

    {
        'especificacao': 'Refrigerante',
        'codigo': 105,
        'preço': 1.00
    }
]

# Mostrar a lista de produto
for chave, produto in enumerate(produtos):
    print(f'Produto {chave + 1}: ')
    print('*' * 20)
    for k, v in produto.items():
        print(f'{k} => {v}')
    print('=' * 50)


codigo = int(input('Digite o codigo do produto: '))

# Buscando pelo produtos que está na list (array)
pos_encontrado = -1
pos = 0

while pos < len(produtos):
    if  produtos[pos].get('codigo') == codigo:
        pos_encontrado = pos
        break
    pos += 1

if pos_encontrado != -1:
    quantidade = int(input('Informe a quantidade: '))
    print(f'========== PREÇO DO PRODUTO =========')
    print(f'Nome do produto: { produtos[pos_encontrado].get("especificacao") }')
    print(f'codigo: { produtos[pos_encontrado].get("codigo") }')
    print(f'preço unitario: R${ produtos[pos_encontrado].get("preço") }')
    print(f'Quantidade informada: {quantidade}')
    print(f'Preço total: R${ produtos[pos_encontrado].get("preço") * quantidade }')
else:
    print(f'<<< Nenhum produto com codigo {codigo} encontrado! >>>')