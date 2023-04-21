def invertido(n):               # a função tem que ser chamada no IDLE
    while True:                 # repeat...until
        print(n % 10, end='')
        n //= 10                # Ou n = n // 10
        if n == 0: break
