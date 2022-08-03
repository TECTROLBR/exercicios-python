print('    CALCULO DO IMC ')
peso = float(input('Qual o seu peso atual? KG '))
altura = float(input('Qual a sua altura? M '))
imc = peso/(altura**2)
print('Seu IMC e de {:.2f} e! '.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você esta no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você esta com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você esta com OBESIDADE')
elif imc > 40:
    print('Você esta com OBESIDADE MÓRBIDA')
