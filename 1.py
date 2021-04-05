numero = int(input("Escolha o numero para ser fatorial "))
count = 1
print(f'{numero}! ', end='')
for i in range(numero - 1, 0, -1):
    count *= i
    resultado = count * numero
    print(f'x {i}', end=' ')
print(f'= {resultado}', end='')
















