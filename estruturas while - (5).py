pt1=int(input('Primeiro termo: '))
ra2=int(input('Razão da PA: '))
cont = 1
print(pt1,end='-')
while cont <10:
    pt1+=ra2
    cont+=1
    print(pt1,end='')
    print('-' if cont < 10 else '= Fim', end='')
