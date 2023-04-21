def soma(a,b):                  # def - Definir função
    c = a + b   
    return c                    # return: dar a resposta,retorna a resposta e 
a = int(input())                # encerra execução.
b = int(input())
print(f'A soma é: {soma(a,b)}') # não utiliza a variável c pq ela esta dentro da
                                # função soma.
