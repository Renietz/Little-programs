


# VARIÁVEIS :


valor_do_produto = float(input('Valor total da compra: R$ '))

# PROGRAMA PRINCIPAL :

if valor_do_produto <= 100:
    print('Desconto aplicado: R${:.2f}'.format(valor_do_produto * .05))
    print('Valor total com desconto: R${:.2f}' .format((valor_do_produto* .95)))

elif valor_do_produto > 100 and valor_do_produto <= 200:
    print('Desconto aplicado: R${:.2f}'.format(valor_do_produto * .10))
    print('Valor total com desconto: R${:.2f}'.format((valor_do_produto * .90)))

elif valor_do_produto >200 and valor_do_produto <=500:
    print('Desconto aplicado: R${:.2f}'.format(valor_do_produto * .15))
    print('Valor total com desconto: R${:.2f}'.format((valor_do_produto * .85)))

else:
    print('Desconto aplicado: R${:.2f}'.format(valor_do_produto * .20))
    print('Valor total com desconto: R${:.2f}'.format((valor_do_produto * .80)))



