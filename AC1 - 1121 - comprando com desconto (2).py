valor = float(input())
q = int(input())
desconto =(valor*q)*(10+q)/100
print(f'{valor*q:.2f}')
print(f'{(valor*q)-desconto:.2f}')
