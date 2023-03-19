nota = float(input('Qual a nota? '))

if nota >=11:
    print('Valor inválido')
else:
    if nota >= 9:
        letra = 'A'
    else:
        if nota >= 8:
            letra = 'B'
        else:
            if nota >= 6:
                letra = 'C'
            else:
                if nota >= 4:
                    letra = 'D'
                else:
                    letra = 'E'

print(f'Sua letra é: {letra}')
