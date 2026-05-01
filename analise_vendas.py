qtd_vendas_2022 = int(input('Digite a quantidade de vendas no ano de 2022: '))
qtd_vendas_2023 = int(input('Digite a quantidade de vendas no ano de 2023: '))

if(qtd_vendas_2022 != 0 and qtd_vendas_2023 != 0):
    variacao = ((100 * qtd_vendas_2023) / qtd_vendas_2022) - 100
    variacao = variacao / 100
    print(f'Variação = {variacao}')

    if(variacao > 0.2):
        print('Bonificação para o time de vendas.')
    elif(0.02 < variacao <= 0.2):
        print('Pequena bonificação para o time de vendas.')
    elif(-0.1 < variacao <= 0.02):
        print('Planejamento de políticas de incentivo às vendas.')
    else:
        print('Corte de gastos.')
else:
    print('Calculo inválido!')
