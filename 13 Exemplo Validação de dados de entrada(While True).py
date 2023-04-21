def somatorio(n):
    soma = 0            # guarda o valor
    qtd = 0             # faz a contagem
    x = 1               # 1º valor positivo
    while qtd < n:
        soma += x
        qtd += 1
        x += 1
    return soma

while True:
    n = int(input('n? '))
    if 0 <= n <= 100: break

print(f'A soma é: {somatorio(n)}')
