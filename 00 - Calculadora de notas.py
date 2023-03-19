ac1, ac2, ac3, ac4 = input('Você fez 5 ACs!\nDigite o valor das quatro maiores notas,dando um espaço entre elas:\n').split()

AC1 = float(ac1)
AC2 = float(ac2)
AC3 = float(ac3)
AC4 = float(ac4)

prova = float(input('Digite agora a nota da sua prova final:\n'))

media_ac = (AC1 + AC2 + AC3 + AC4) / 4
media_final = (media_ac + prova) / 2

if media_final >= 6:
    print(f'Sua média final foi {media_final:.1f}''\n''Parabéns, Você passou nesta disciplina!')
else:
    print(f'Sua média final foi {media_final:.1f}''\n''Sinto muito,mas você precisa estudar mais!''\n''Nos vemos no próximo semestre!')
