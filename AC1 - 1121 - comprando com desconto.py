valor = float(input())
q = int(input())
dvalor =(valor*q)*10/100
dq = (valor*q)*q/100
print(f'{valor*q:.2f}')
print(f'{(valor*q)-dvalor-dq:.2f}')
