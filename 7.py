# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
# deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
count = 0
i = 1
n = int(input("Fale um nomero inteiro "))
while i < n:
    for i in range(1, n + 1):
        for c in range(1, n + 1):
            if i % c == 0:
                count += 1
        if count <= 2:
            print(f'{i} é primo, não foi divisivel por mais de 2 {count} numeros')
        elif count > 2:
            print(f"{i} não é primo, foi divisivel o {count} numeros")
        count = 0
