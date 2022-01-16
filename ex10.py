saldo_medio = float(input('Informe o saldo médio: '))

# Tirar o sinal negativo caso o usuário informar numero negativo
saldo_medio *= (-1) if saldo_medio < 0 else 1

if saldo_medio <= 200:
    porcentagem_credito = 0
elif saldo_medio <= 400:
    porcentagem_credito = 20
elif saldo_medio <= 600:
    porcentagem_credito = 30
else:
    porcentagem_credito = 40

print('====== INFORMAÇÃO =====')
print(f'Saldo médio: R${saldo_medio}')
print(f'Credito: R${saldo_medio * porcentagem_credito / 100 }')