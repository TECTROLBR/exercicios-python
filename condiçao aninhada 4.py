print('   Anlizando notas')
nota1 = float(input('nota 1? = '))
nota2 = float(input('Nota 2? = '))
media = (nota1 + nota2)/2
if media <= 5.0:
    print('Sua media foi {}'.format(media))
    print('Você foi reprovado!')
elif  media >=5.1 and media<=6.9 :
    print('sua media foi {}'.format(media))
    print('Você esta de recuperação!')
elif media >= 7.0 :
    print('Sua media foi {}'.format(media))
    print('Você foi aprovado!')
print(media)
