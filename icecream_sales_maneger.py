

# MENU:
print(' ')
print('Bem-vindo a Sorveteria do Matheus Nuernberg Steiner')
print(' ')

print('-' * 44, 'Cardápio', '-' * 44)
print('|', 'Código  ', '|', 'Descrição           ', ' |', 'Tamanho P (500ml)', '|', 'Tamanho M (1000ml)', '|',
      'Tamanho G (1000ml)', '|')
print('|', '   TR   ', '|', 'Sabores Tradicionais', ' |', '     R$ 6,00     ', '|', '      R$10,00    ',
      ' |''       R$18.00     ', '|')
print('|', '   ES   ', '|', 'Sabores Especiais', '    |', '     R$ 7,00     ', '|', '      R$12,00    ',
      ' |''       R$21.00     ', '|')
print('|', '   PR   ', '|', 'Sabores Premium  ', '    |', '     R$ 8,00     ', '|', '      R$14,00    ',
      ' |''       R$24.00     ', '|')
print('-' * 98)

# variáveis:


while True:
    menu = input('Entre com o TAMANHO do pode desejado (P/M/G): ')
    codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')
    if menu  == 'p' and codigo == 'tr':
        print('Você pediu um sorvete sabor Tradicional P de R$ 6,00')
        soma+=6
        print('-' * 49)
    elif menu == 'm'and codigo == 'tr':
        print('Você pediu um sorvete sabor Tradicional M de R$ 10,00')
        soma += 10
        print('-' * 49)
    elif menu == 'g' and codigo == 'tr':
         print('Você pediu um sorvete sabor Tradicional G de R$ 18,00')
         soma += 18
         print('-' * 49)

    elif menu == 'p' and codigo == 'es':
        print('Você pediu um sorvete sabor Especial P de R$ 7,00')
        soma += 7
        print('-' * 49)
    elif menu == 'm' and codigo == 'es':
        print('Você pediu um sorvete sabor Especial M de R$ 12,00')
        soma += 12
        print('-' * 49)
    elif menu == 'g' and codigo == 'es':
        print('Você pediu um sorvete sabor Especial G de R$ 21,00')
        soma += 21
        print('-' * 49)

    elif menu == 'p' and codigo == 'pr':
        print('Você pediu um sorvete sabor Premium P de R$ 8,00')
        soma += 8
        print('-' * 49)
    elif menu == 'm' and codigo == 'pr':
        print('Você pediu um sorvete sabor Premium M de R$ 14,00')
        soma += 14
        print('-' * 49)
    elif menu == 'g' and codigo == 'pr':
        print('Você pediu um sorvete sabor Premium G de R$ 24,00')
        soma += 24
        print('-'*49)

    else:
        print('!'*7+' ','Tamanho ou CÓDIGO INVÁLIDOS(S)',' '+7*'!')
        continue

    menu_c = input('Deseja pedir mais alguma coisa? (S/N):')

    if menu_c == 's':
     continue


    if menu_c == 'n':
     print ('O total a ser pago é:{}'.format(soma))
    break







