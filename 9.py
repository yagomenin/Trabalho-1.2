# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme
# a média calculada.
r = 's'
count = 0
soma = 0
resultado = 0
while r == 's':
    n = int(input("Fale quantas pessoas a na turma????? "))
    soma = n
    for i in range(1, n + 1):
        n = float(input("Fale a idade das pessoas? "))
        count += n
        resultado = count / soma
    if resultado > 0 and resultado < 25:
        print(f"Sua turma tem uma média de idade de {resultado}, então é considerada jovem ")
    elif resultado > 25 and resultado < 60:
        print(f"Sua turma tem uma média de idade de {resultado}, então é considerada adulta ")
    elif resultado > 60:
        print(f"Sua turma tem uma média de idade de {resultado}, então é considerada idosa ")
    r = input("Você quer cadastras outra turma? ")
else:
    if r == 'n':
        print("Suas turmas foram cadastradas, até a proxima")
