total = 0 # variável acumulativa
preco = float(input('preço do item: '))

while preco != -1:
    total += preco
    preco = float(input('preco do item: '))
print(f'total da compra: R$ {total:.2f}')
