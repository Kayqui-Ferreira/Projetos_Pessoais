from random import choice
print('BEM VINDO AO TESTE DE PROBABILIDADE !!!!!')
print('='*40)
print('Iremos lançar um dado de 6 lados iguais')
print('')
E = int(input('Escolha um número de 1 a 6 para tentar a sorte: '))
P = (1/6)*100
print(f'A probabilidade de cair o número {E} é de {int(P)}%')
print('')
input('Aperte Enter para tentar a sorte')
print('')
l = [1,2,3,4,5,6]
sorteio = choice(l)
print(f'O número sorteado foi: {sorteio}')
if sorteio == E:
    print('PARÁBENS, SORTE ESTÁ DO SEU LADO !!')
else:
    print('Que pena, não foi dessa vez... Mas não desista, Tente novamente.')
print('')
print('='*40)