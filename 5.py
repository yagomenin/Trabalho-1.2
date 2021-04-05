# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
count = 0
n = float(input("Fale um nomero inteiro "))
while n // 1 != n:
    n = float(input("Fale um numero inteiro apedeuta "))
else:
    n = int(n)
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            print(i)
    if count <= 2:
        print(f"{n} é primo")
    else:
        print(f'{n} não é primo')





