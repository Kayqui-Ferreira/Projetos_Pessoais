from math import sqrt
CA = float(input('Digite o valor do Cateto Adjacente: '))
CO = float(input('Digite o valor do Cateto Oposto: '))
H = CA**2+CO**2
print(f'O triângulo com o Cateto adjacente igual a {CA} e o Cateto Oposto igual a {CO}, tem uma Hipotenusa igual a: {sqrt(H):.2f}')