import random
aluno1=str(input(print('digite o nome do aluno ')))
aluno2=str(input(print('digite o nome do aluno ')))
aluno3=str(input(print('digite o nome do aluno ')))
aluno4=str(input(print('digite o nome do aluno ')))
lista=[aluno4,aluno3,aluno2,aluno1]
ale = random.choice(lista)
print('entao quem vai apaga o quador e {}?'.format(ale))