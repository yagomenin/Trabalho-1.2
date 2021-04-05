# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de
# quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado
# o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar
# na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os
# preços de 1 até 50 produtos, conforme o exemplo abaixo:

n = 0
div = 1
itens_loja = 1.99
r = 's'
while r == 's':
    n = int(input("Quantos itens você vai levar hj? "))
    while n == 0 or n > 50:
        if n == 0:
            n = int(input("Voce deve levar ao minimo 1 item "))
        else:
            n = int(input("Você não pode levar de 50 itens, escolha seus itens novamente "))
    else:
        div = n * itens_loja
        print(f"Sua conta deu {div} R$", end=" ")
        print("Obrigado pela compra!!!!!")
    r = input("Há mais alguem na fila: s/n ")
else:
    if r == 'n':
        print("Como não há nimguem na fila: Programa Desliga")






