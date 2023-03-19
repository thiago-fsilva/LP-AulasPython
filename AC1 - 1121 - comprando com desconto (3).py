valor = float(input())
qntd = int(input())
total = valor * qntd
desconto = total * 0.1
desconto_quantidade = total * (qntd*0.01)
print(f'{total:.2f}')
print(f'{total-desconto-desconto_quantidade:.2f}')
