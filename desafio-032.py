import calendar
ano = int(input('Digite o ano que quer verificar? '))
anoB = calendar.isleap(ano)
if anoB is True:
    print(f'O ano {ano} É BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')