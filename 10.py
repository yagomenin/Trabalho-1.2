# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato.

r = 's'
Darci = 0
Luian = 0
Bilaque = 0
while r == 's':
    n = int(input("Quantos eleitores há????? "))
    for i in range(1, n + 1):
        n = float(input("Para votar para Darci = 1, para Luian = 2 e para Bilaque = 3? "))
        if n == 1:
            Darci += 1
        elif n == 2:
            Luian += 1
        elif n == 3:
            Bilaque += 1
    if Darci > Luian and Darci > Bilaque:
        print(f'Darci é o vencedor com {Darci} votos,luian fez {Luian} votos e Bilaque fez {Bilaque} votos')
    elif Luian > Darci and Luian > Bilaque:
        print(f'Luian é o vencedor com {Luian} votos,Darci fez {Darci} votos e Bilaque fez {Bilaque} votos')
    else:
        print(f'Bilaque é o vencedor com {Bilaque} votos,luian fez {Luian} votos e Darci fez {Darci} votos')
    r = input("Acha que foi roubado, digite s para refazer e n para terminar: s/n ")
else:
    if r == 'n':
        print("As eleições terminaram ")




