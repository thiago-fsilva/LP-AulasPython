def qtd_divisores(x):
    qtd = 0
    candidato = 1
    while candidato <= x:
        if x % candidato == 0:
            qtd += 1
        candidato += 1
    return qtd

x = int(input('x?'))
qtd = qtd_divisores(x)

if qtd == 2:
    print('é primo')
else:
    print('não é primo')
