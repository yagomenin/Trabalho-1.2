# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.
r = input("Quer começar s ou n ")
numero = 0
count = 1
resultado = 0
while r == 's':
    numero = (input("Escolha o numero para ser fatorial "))
    while not numero.isnumeric():
        numero = (input("Tem que ser um numero seu Apedeuta!! "))
    else:
        numero = float(numero)
        while numero < 0 or numero > 16:
            numero = float(input("Você errou apedeuta, tente novamento um numero menor que 16 e positivo!!! "))
        else:
            while numero // 1 != numero:
                numero = float(input("Informe um numero inteiro apedeuta "))
            else:
                numero = int(numero)
                print(f'{numero}! ', end='')
                for i in range(numero - 1, 0, -1):
                    count *= i
                    resultado = count * numero
                    print(f'x {i}', end=' ')
        print(f'= {resultado} ')
        count = 1
    r = input("Quer calcular outro numero ")
else:
    if r == 'n':
        print("Seus calculos foram completados, até a proxima")

