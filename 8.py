# Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Fale quantas notas dejesa registar?????"))

count = 0
soma = n
for i in range(1, n + 1):
    n = float(input("Fale as nota aqui"))
    if n == float(n):
        count += n
print(count / soma)
