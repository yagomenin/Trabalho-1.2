g = 0
count = 0
box = 0
maior = 0
menor = 0
r = input("Quer começar a escolhar seu conjuntos de numeros?? s/n ")
while r == "s":
        g = int(input("Escolha seus numeros "))
        count += g
        box += 1
        if box == 1:
                maior = g
                menor = g
        else:
                if g > maior:
                        maior = g
                if g < menor:
                        menor = g
        r = input("Voce quer continuar ")
print(f'A soma dos seus numeros foi de {count}', end=" ")
print(f'E o maior numero digitado foi {maior}', end= " ")
print(f', e o menor numero foi {menor}')












