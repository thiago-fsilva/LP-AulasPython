i = int(input())
f = int(input())
bi = 0

while i <= f:
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print(i)
        bi += 1
    i += 1

print(f'bissextos: {bi}')
