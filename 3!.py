# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
box = 0
count = 0
maior = 0
menor = 0
r = input("Quer começar a escolhar seu conjuntos de numeros?? s/n ")
while r == "s":
        g = int(input("Escolha seus numeros, eles podem ser de 0 até 1000 "))
        while g < 0 or g > 1000:
                g = int(input("Errado apedeuta,coloque numero de 0 até 1000 "))
        else:
            count += g
            box += 1
            r = input("Voce quer continuar ")
            if box == 1:
                maior = g
                menor = g
            else:
                if g > maior:
                    maior = g
                if g < menor:
                    menor = g

print(f'A soma dos seus numeros foi de {count}')
print(f' Maior numero foi {maior}')
print(f' e menor numeor foi de {menor}')
