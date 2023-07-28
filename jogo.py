


#vamos importar o módulo random
from random import randint
#importar o módulo time para cadenciar o nome joquempo
from time import sleep

#definindo os itens
itens =('pedra','papel','tesoura')

#jogada do computador
computador = randint(0,2)

#apresentar as opções:
print('Suas opcoes: '
      '[0]PEDRA'
      '[1]PAPEL'
      '[2]TESOURA ')

#AGORA O JOGADOR FAZ A JOGADA...

jogador=int(input('Qual a sua jogada' ))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=' * 11)

#mostrando o que cada um jogou...
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)

#montar estruturas condicionais para apresentar resultados
if computador == 0: # computador jogou pedra
    if jogador ==0:
        print('EMPATE')

    elif jogador ==1:
        print('JOGADOR VENCE!')

    elif jogador ==2:
        print('COMPUTADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')

if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE!')

    elif jogador == 2:
        print('COMPUTADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')

    elif jogador == 1:
        print('COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA!')