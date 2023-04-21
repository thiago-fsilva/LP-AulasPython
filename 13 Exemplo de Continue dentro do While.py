credito = float(input('Seu crédito? R$'))
while credito > 0:
    item = float(input('Preço do item? R$'))
    if item > credito:
        print('Compra negada! Ultrapassa seu crédito')
        continue
    credito -= item
print(f'Você utilizou todo seu crédito')
