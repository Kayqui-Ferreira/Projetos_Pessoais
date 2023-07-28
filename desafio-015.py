D = int(input('Digite quantos dias foram alugados: '))
KM = float(input('Digite quantos KM foram rodados: '))
V = (D*60)+(KM*0.15)
print(f'O aluguel de {D}dias de um automovel com {KM}KM´s rodados será no valor de R${V:.2f}')