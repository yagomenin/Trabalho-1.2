# aça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
# de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

r = 's'
count = 0
soma = 0
resultado = 0
while r == 's':
    n = int(input("Fale quantas turmas há????? "))
    soma = n
    for i in range(1, n + 1):
        n = float(input("Fale quantas pessoas há por turma ? "))
        while n > 40:
            n = float(input("Só ter no max 40 pessoas por turma, tente novamente "))
        else:
            count += n
            resultado = count / soma
    print(f"A media por turma é de {resultado}")
    r = input("Deseja fazer outro cadastramento: s/n ")
else:
    if r == 'n':
        print("Suas turmas foram cadastradas")
