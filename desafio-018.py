from math import sin, cos, tan, radians
A = float(input('Digite o valor do ângulo: '))
S = sin(radians(A))
C = cos(radians(A))
T = tan(radians(A))
print(f'O triângulo de ângulo {A} terá:')
print(f' Seno igual a {S:.2f}\n Cosseno igual a {C:.2f}\n Tangente igual a {T:.2f} ')