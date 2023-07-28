v = float(input('Qual era sua velocidade: '))
multa = (v-80)*7
print('-'*35)
if v > 80:
    print('A velocidade MÁXIMA permitida é de 80 KM/h.')
    print(f'Como você ultrapassou esse limite, terá de pagar uma multa no valor de R${multa:.2f}, equivalentes á cada KM a cima do permitido.')
    print('Tenha mais cuidado com a velocidade da Rodovia.')
else:
    print('Tenha um bom dia e siga com segurança !')