def exibe_bi(i, f):
    while i <= f:
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            a = print(i)
        i += 1

def qnt_bi(i, f):
    qnt = 0
    while i <= f:
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            qnt += 1
        i += 1
    return qnt

i = int(input())
f = int(input())

exibe_bi (i, f)
print(f'bissextos: {qnt_bi(i, f)}')
