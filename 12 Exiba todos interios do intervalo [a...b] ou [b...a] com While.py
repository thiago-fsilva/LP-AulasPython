a = int(input())
b = int(input())


if a < b:
    x = a
    while x <= b:
        print(x)
        x += 1
    print('FIM')
else:
    x = b
    while x <= a:
        print(x)
        x += 1
    print('FIM')
