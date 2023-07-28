from time import sleep as s
n = int(input('Digite um número: '))
r = n % 2
print('-'*30)
print(f'Análisando o número {n}...')
s(2)
print('-'*30)
if r == 0 :
    print(f'O número {n} é PAR.')
else:
    print(f'O número {n} é IMPAR.')