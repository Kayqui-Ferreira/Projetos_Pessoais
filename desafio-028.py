from random import randint as a
from time import sleep

print('Vamos jogar um jogo.')
print("-"*30)

print('HUM...Pensei em um número de 1 a 5')
s = a(1,5)
n = int(input('Qual número você acha que eu pensei ? '))
print('-'*30)
print('PROCESSANDO...')
sleep(3)
if s == n:
    print('-'*30)
    print('AHHHHH... Você me venceu!')
else:
    print('-'*30)
    print(f'Dessa vez eu ganhei! pensei no número {s}, não no número {n}.')

