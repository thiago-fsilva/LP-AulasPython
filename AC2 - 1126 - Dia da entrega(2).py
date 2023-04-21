dia = input(str())
p = int(input())
a = 'domingo'
b = 'segunda'
c = 'terca'
d = 'quarta'
e = 'quinta'
f = 'sexta'
g = 'sabado'
if p == 0:
    print('chega hoje!')
elif dia == b and p == 6 or dia == c and p == 5 or dia == d and p == 4 or dia == e and p == 3 or dia == f and p == 2 or dia == g and p == 1:
    print(f'sera entregue domingo')
elif dia == c and p == 6 or dia == d and p == 5 or dia == e and p == 4 or dia == f and p == 3 or dia == g and p == 2 or dia == a and p == 1:
    print(f'sera entregue segunda')
elif dia == d and p == 6 or dia == e and p == 5 or dia == f and p == 4 or dia == g and p == 3 or dia == a and p == 2 or dia == b and p == 1:
    print(f'sera entregue terca')
elif dia == e and p == 6 or dia == f and p == 5 or dia == g and p == 4 or dia == a and p == 3 or dia == b and p == 2 or dia == c and p == 1:
    print(f'sera entregue quarta')
elif dia == f and p == 6 or dia == g and p == 5 or dia == a and p == 4 or dia == b and p == 3 or dia == c and p == 2 or dia == d and p == 1:
    print(f'sera entregue quinta')
elif dia == g and p == 6 or dia == a and p == 5 or dia == b and p == 4 or dia == c and p == 3 or dia == d and p == 2 or dia == e and p == 1:
    print(f'sera entregue sexta')
else:
    print(f'sera entregue sabado')
