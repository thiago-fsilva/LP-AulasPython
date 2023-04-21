x = int(input())    # 7 - 2 = 5 | 1
y = int(input())    # 5 - 2 = 3 | 1
q = 0               # 3 - 2 = 1 | 1
                    # 1 resto
while x >= y:       # Total     | 1+1+1 = 3
    x -= y
    q += 1
print(q)
