a = int(input('Digite o Primeiro número: '))
b = int(input('Digite o Segundo número: '))
c = int(input('Digite o Terceiro número: '))
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'o menor número é o número {menor}')
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior número é o número {maior}')