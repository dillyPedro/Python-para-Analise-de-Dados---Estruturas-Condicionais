escolha = input('Escolha se deseja abastecer por Etanol (E) ou Diesel (D): ').lower()

if(escolha not in {'e', 'd'}):
    print('Escolha inválida!!!')
else:
    if(escolha == 'e'):
        preco_etanol = 1.70
        qtd_litros = float(input('Digite a quantidade de litros que gostaria de abastecer: '))
        if(qtd_litros <= 15):
            desconto = preco_etanol * qtd_litros * 0.02
            print(f'Valor total do desconto = {desconto}')
        else:
            desconto = preco_etanol * qtd_litros * 0.04
            print(f'Valor total do desconto = {desconto}')
        valor_pago = (preco_etanol * qtd_litros) - desconto
        print(f'Valor total a ser pago no etanol = R${valor_pago}')
    else:
        preco_diesel = 2.00
        qtd_litros = float(input('Digite a quantidade de litros que gostaria de abastecer: '))
        if(qtd_litros <= 15):
            desconto = preco_diesel * qtd_litros * 0.03
            print(f'Valor total do desconto = {desconto}')
        else:
            desconto = preco_diesel * qtd_litros * 0.05
            print(f'Valor total do desconto = {desconto}')
        valor_pago = (preco_diesel * qtd_litros) - desconto
        print(f'Valor total a ser pago no diesel = R${valor_pago}')

print('\nFim do calculo!!!')
