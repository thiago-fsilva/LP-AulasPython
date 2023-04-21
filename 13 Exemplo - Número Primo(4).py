def qtd_divisores(x):
    qtd = 0
    candidato = 1
    while candidato <= x:
        if x % candidato == 0:
            qtd += 1
        candidato += 1
    return qtd

def primo (x):
    return qtd_divisores(x) == 2

x = int(input('x?'))

if primo(x):
    print('é primo')
else:
    print('não é primo')
