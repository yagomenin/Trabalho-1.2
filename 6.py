# Altere o programa de cálculo dos números primos,
# informando, caso o número não seja primo, por quais número ele é divisível.]
count = 0
box = tuple()
n = int(input("Fale um nomero inteiro "))
for c in range(1, n + 1):
    if n % c == 0:
        box += (c,)
        count += 1
if count > 2:
    print(f"{n} não é primo e foi divisel por {box}")
if count <= 2:
    print(f'{n} é primo')











