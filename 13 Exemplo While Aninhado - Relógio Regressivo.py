h = 23
while 0 <= h:
    m = 59
    while 0 <= m:
        s = 59
        while 0 <= s:
            print(f'{h:02}:{m:02}:{s:02}')
            s -= 1
        m -= 1
    h -= 1
