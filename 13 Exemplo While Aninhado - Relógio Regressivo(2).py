h = 23
while h > -1:
    m = 59
    while m > -1:
        s = 59
        while s > -1:
            print(f'{h:02}:{m:02}:{s:02}')
            s -= 1
        m -= 1
    h -= 1
