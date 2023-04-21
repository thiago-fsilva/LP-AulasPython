vic = float(input())
total = 0

while vic != -1.0:
    total += vic
    vic = float(input())
print(f'VC$ {total:.2f}')
print(f'R$ {(total*2.50):.2f}')
