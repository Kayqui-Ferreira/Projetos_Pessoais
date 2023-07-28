km = float(input('Qual é a distância da sua viagem em KM: '))
if km <= 200:
    print(f'O valor da passagem para sua viagem será de R${km*0.50:.2f}')
else:
    print(f'O valor da passagem para sua viagem será de R${km*0.45:.2f}')