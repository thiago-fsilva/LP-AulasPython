nota_trab = float(input())
prova_reg = float(input())
mediafinal = (nota_trab + prova_reg) / 2
mediafsub = (nota_trab + 10) / 2

if mediafinal >= 6:
    print('aprovado')
elif mediafinal <6 and mediafsub >= 6:
    print('talvez com a sub')
else:
    print('reprovado')
