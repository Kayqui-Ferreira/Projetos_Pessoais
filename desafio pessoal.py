from random import randint as a
from time import sleep

print('Vamos jogar um jogo.')
print("-" * 30)

print('HUM...Pensei em um número de 1 a 5')
s = a(1, 5)
n = int(input('Qual número você acha que eu pensei ? '))
print('-' * 30)

while n > 5:
    print(f'Ops! {n} não é uma resposta válida')
    print('Tente novamente')
    n = int(input('Qual número você acha que eu pensei ? '))

print('PROCESSANDO...')
sleep(2)

if n == s:
    print('Parabens! Você acertou!!!!')
else:
    print('Putz não foi dessa vez')


r = input('Quer tentar novamente, sim ou não?').strip()
rs = ('sim' or 's' in r)
while r is True:
    n = int(input('Qual número você acha que eu pensei ? '))
    print('Parabens! Você acertou!!!!')
    break

print('Nos vemos na próxima!!')
