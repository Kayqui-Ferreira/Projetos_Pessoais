r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
 print(f' as retas {r1}, {r2} e {r3} PODEM formar um triângulo.')
else:
    print(f'As retas {r1}, {r2} e {r3} NÃO pode formar um triâmgulo')