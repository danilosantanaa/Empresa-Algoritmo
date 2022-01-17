segundos = int(input('Digite o tempo em segundo: '))

horas  = 0
minutos = 0

if segundos >= 3600:
    horas = int(segundos / 3600)
    segundos -= horas * 3600
if segundos >= 60:
    minutos = int(segundos / 60)
    segundos -= minutos * 60

print('=' * 60)
print(f'Expresso em formato de hora fica: {horas}horas {minutos}min {segundos}segundos')
