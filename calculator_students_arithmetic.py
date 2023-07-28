# VARIÁVEIS :
print('')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))
media = ((nota1 + nota2 + nota3 + nota4) /4)

print('')

#PROGRAMA PRINCIPAL:
if media >= 7:
    print('Média aritmética: {}'.format(media))
    print('Aluno aprovado')

else:
    print('Média aritmética: {}'.format(media))
    print('Aluno reprovado')
