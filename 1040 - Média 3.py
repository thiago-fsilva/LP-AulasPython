n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media_n = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / (2+3+4+1)

print(f'{media_n:.1f}')

if 5.0 <= media_n <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    if (nota_exame*media_m)/2 >= 5.0:
        print(f'Nota do exame: {nota_exame}')
        print('Aluno aprovado')
    else:
        print(f'Nota do exame: {nota_exame}')
        print('Aluno reprovado')
