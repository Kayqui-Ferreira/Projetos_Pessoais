salario = float(input('Digite o seu salário inicial: R$'))
if salario >= 1250.00 :
    print(f'Seu novo salário é de R$ {(salario*0.10) + salario:.2f}')
else:
    print(f'Seu novo salário é de R$ {(salario*0.15) + salario:.2f}')
print('')
print('PARABENS !!!')