# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
# em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
r = 's'
count = 0
cd = 1.60
while r == 's':
    n = int(input("Quantos colecionadores há? "))
    div = n
    for c in range(1, n + 1):
        n = int(input("Quantos cds este colecionador comprou, cd vale 1.60 atualmente ???? "))
        soma = n * cd
        count += soma
        (print(f'Ele gastou {soma} R$ em sua coleção de cds'))
    print(f"Estes {div} colecionadores, gastaram o tolal de {count} R$ em cds, e a media total foi de {round(count / div)} R$")
    r = input("Voce que cadastrar novos colecionadores: s/n ")
else:
    if r == 'n':
        print("Colecionadores gastaram muito em suas coleções, obrigado e até a proxima ")








