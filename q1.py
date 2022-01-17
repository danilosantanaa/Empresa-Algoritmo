from datetime import date

# Verificar se o ano é bissexto
def isAnoBissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 1 ) or ano % 400 == 0

# Funcao que retorna a quantidade de dias de acordo com o mes
def qtdMesDia(mes, ano):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
       return  30
    else:
        return 29 if isAnoBissexto(ano) else 28

# Obtendo a quantidade de dias no intervalo tal que ano < i < 2022 para pegar a quantidade de dia inteira sem parte dos intervalo
def qtdDiaIntervalAnos(ano_maior, ano_menor):
    qtd_dia_sobras = 0

    # Obtendo a quantidade de dias nos anos que são bissextos no intervalo de  ano < i < 2022
    for i in range(ano_menor + 1, ano_maior):
        if isAnoBissexto(i):
            qtd_dia_sobras += 1
    
    return ( ano_maior - ano_menor - 1 ) * ( 365 if ano_maior != ano_menor else 0 ) + qtd_dia_sobras

# Função que tem como objetivo pegar a quantidade de dias dos anos que não tem 365 ou 366 dias 
# Tal que mes < i <= 12
def qtdDiaAnoQuebrado(ano, dia, mes, is_soma = False):
    qtd_dias = 0
    if is_soma or ano == date.today().year:
        for i in range(1, mes):
            qtd_dias += qtdMesDia(i, ano)
    else:
        for i in range(mes + 1, 13):
            qtd_dias += qtdMesDia(i, ano)

    # Caso for o ano atual, subtrair a data invez de somar
    if not is_soma and ano == date.today().year and mes == date.today().month:
        dia = date.today().day - dia

   
    return qtd_dias + ( dia if is_soma or ano == date.today().year else qtdMesDia(mes, ano) - dia )

# Funcao que retorna a quantidade de dias
def qtdDias(ano, mes, dia):
    # Obtendo a data atual
    ano_atual  = date.today().year
    mes_atual = date.today().month
    dia_atual = date.today().day


    dias = 0
    if ano == ano_atual:
        dias = qtdDiaAnoQuebrado(ano_atual, dia_atual, mes_atual, True) - qtdDiaAnoQuebrado(ano, dia, mes, True)
    else:
        dias = qtdDiaAnoQuebrado(ano_atual, dia_atual, mes_atual, True) + qtdDiaAnoQuebrado(ano, dia, mes)

    
    return  qtdDiaIntervalAnos(ano_atual, ano) + dias

ano_atual  = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day

# Lendo as datas
while True:
    try:
        ano = int(input('Digite o ano: '))

        if ano > 0 and ano <= date.today().year:
            break
        else:
            print(f'<<< ERRO! Por favor informe o ano no intervalo de 1 até {date.today().year}')
    except ValueError:
        print('<<< ERRO! Por favor informe um numero inteiro para o ano. >>>')

while True:
    try:
        mes = int(input('Digite o mes: '))

        if mes >= 1 and mes <= 12 and ano != ano_atual or mes >=1 and mes <= mes_atual and ano == ano_atual:
            break
        else:
            print(f'<<< ERRO! Por favor informe o mes no intervalo de 1 até { mes_atual if ano == ano_atual else 12 }')
    except ValueError:
        print('<<< ERRO! Por favor informe um numero inteiro para o mes. >>>')

while True:
    try:
        dia = int(input('Digite o dia: '))

        if dia <= qtdMesDia(mes, ano) and not ( mes_atual == mes and ano_atual == ano )  or mes_atual == mes and ano_atual == ano and dia_atual >= dia:
            break
        else:
            print(f'<<< ERRO! Informe data do mes { mes } do intervalo de 1 até {date.today().day if  date.today().month == mes and date.today().year == ano else qtdMesDia(mes, ano) }. >>>')
    except ValueError:
        print('<<< ERRO! Por favor informe um numero inteiro para o dia. >>>')

print('=' * 50)
print(f'Convertendo a idade fica em: {qtdDias(ano, mes, dia)} dias de idade.')