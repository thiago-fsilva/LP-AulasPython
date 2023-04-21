n = int(input())
qnt = 0
a = 0

if 0 < n <= 26:
    while qnt < n:
        qnt += 1
        a += 1
        print(a*chr(64+a))
