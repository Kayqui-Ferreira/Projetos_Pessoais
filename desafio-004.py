a = input('Digite algo: ')
print(f'O tipo de {a} é', type(a))
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('Está apenas em Maiúsculas?', a.isupper())
print('Está apenas em Minúsculas?', a.islower())
print('Contém apenas espaços?', a.isspace())