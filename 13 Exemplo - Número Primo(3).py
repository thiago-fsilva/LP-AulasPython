def qtd_divisores(x):
    qtd = 0
    candidato = 1
    while candidato <= x:
        if x % candidato == 0:
            qtd += 1
        candidato += 1
    return qtd

def primo (x):
    if qtd_divisores(x) == 2:
        return True
    else:
        return False

x = int(input('x?'))

if primo(x):
    print('é primo')
else:
    print('não é primo')
