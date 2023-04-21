def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
qnt = 0
if par(a):
    qnt += 1
if par(b):
    qnt += 1
if par(c):
    qnt += 1
if par(d):
    qnt += 1
if par(e):
    qnt += 1
print(f'{qnt} valores pares')
