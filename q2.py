from datetime import date

# Verificar se o ano é bissexto
def isAnoBissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 1 ) or ano % 400 == 0

# Funcao que retorna a quantidade de dias de acordo com o mes
def qtdMesDia(mes, ano):
    tot_dia_mes = [31, (29 if isAnoBissexto(ano) else 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return tot_dia_mes[mes - 1]

# OK Função que tem como objetivo pegar a quantidade de dias dos anos que não tem 365 ou 366 dias 
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

# OK Obtendo a quantidade de dias no intervalo tal que ano < i < 2022 para pegar a quantidade de dia inteira sem parte dos intervalo
def qtdDiaIntervalAnos(ano_maior, ano_menor):
    qtd_dia_sobras = 0

    # Obtendo a quantidade de dias nos anos que são bissextos no intervalo de  ano < i < 2022
    for i in range(ano_menor + 1, ano_maior):
        if isAnoBissexto(i):
            qtd_dia_sobras += 1
    
    return ( ano_maior - ano_menor) * ( 365 if ano_maior != ano_menor else 0 ) + qtd_dia_sobras


# Funcao que obtem dia, mes e ano dados uma quantidade de dias
def getAnoMesDia(totDias):
    ano_atual = date.today().year
    mes_atual = date.today().month
    dia_atual = date.today().day

    # Obtendo o ano inteiro se a quantidade de dias tem 2022 dias, ano sera 2017
    ano = ano_atual - ( totDias // 365 )

    # Obtendo a quantidade de dias do ano ate ano_atual.
    qtd_dias_sobras = qtdDiaIntervalAnos(ano_atual, ano)

    # Obtendo os dias que sobrou
    dias_sobras = ( totDias - qtd_dias_sobras ) - qtdDiaAnoQuebrado(ano_atual, dia_atual, mes_atual, True)

    # Descobrir o mes quando dias_sobras - QTD_DIA(MES) > 0
    # Caso o ano descoberto seja diferente do ano atual
    if ano - 1 != ano_atual and dias_sobras >= 0:
        mes_pos = 12
        ano -= 1
        while True:
            if not ( mes_pos > 1 and  dias_sobras > qtdMesDia(mes_pos, ano) ):
                break

            dias_sobras -= qtdMesDia(mes_pos, ano)
            mes_pos -= 1
        
        dias_sobras = qtdMesDia(mes_pos, ano) - dias_sobras

    # Caso seja o mesmo ano 
    else:
        mes_pos = 1
        dias_sobras *= (-1)
        while True:
            if not ( mes_pos < 12 and dias_sobras > qtdMesDia(mes_pos, ano) ):
                break
            dias_sobras -= qtdMesDia(mes_pos, ano)
           
            mes_pos += 1

        
    
    return f'{ ano }/{ mes_pos }/{dias_sobras }'


dias = int(input('Digite a quantidade de dias: '))
print('=' * 50)
print(f'Convertendo a idade {dias} dias de idade em formato de data fica: ')
print(f'Data de Nascimento: {getAnoMesDia(dias)}')

