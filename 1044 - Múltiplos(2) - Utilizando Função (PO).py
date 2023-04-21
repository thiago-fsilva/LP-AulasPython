def divisivel(x,y):
    if x % y == 0:
        return True
    else:
        return False

a, b = input().split()
a = int(a)
b = int(b)

if divisivel(a, b) or divisivel(b, a):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
