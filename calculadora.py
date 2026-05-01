print('-------------------------------------------------------')
print('              BEM VINDO A CALCULADORA')
print('-------------------------------------------------------')

print('Opções de Calculo da Calculadora: ')
print('+: Soma entre os números: ')
print('-: Subtração entre os números: ')
print('*: Multiplicação entre os números: ')
print('/: Divisão entre os números: ')

num1 = int(input('Escolha o primeiro número: '))
num2 = int(input('Escolha o segundo número: '))

opc = input('Escolha o calculo que deseja efetuar (+, -, * ou /): ')

if opc in {'+', '-', '*', '/'}:
    if(opc == '+'):
        resultado = num1 + num2
        print(f'O resultado da soma entre {num1} + {num2} = {resultado}')
    elif(opc == '-'):
        resultado = num1 - num2
        print(f'O resultado da subtração entre {num1} - {num2} = {resultado}')
    elif(opc == '*'):
        resultado = num1 * num2
        print(f'O resultado da multiplicação entre {num1} * {num2} = {resultado}')
    elif(opc == '/'):
        if(num2 != 0):
            resultado = num1 / num2
            print(f'O resultado da divisão entre {num1} / {num2} = {resultado}')
        else:
            print('Ocorreu um erro, pois temos uma divisão por 0.')
    else:
        print('Opção escolhida é inválida.')

    if(resultado.is_integer()):
        if(resultado % 2 == 0):
            print(f'O resultado {resultado} é PAR!!!')
        else:
            print(f'O resultado {resultado} é IMPAR!!!')
    else:
        print(f'O numero {resultado} é decimal e por isso não se classifica como PAR ou IMPAR.')

    if(resultado > 0):
        print(f'O resultado {resultado} é positivo.')
    elif(resultado < 0):
        print(f'O resultado {resultado} é negativo.')
    else:
        print(f'O resultado é igual a 0.')

    if(resultado.is_integer()):
        print(f'O número {resultado} é inteiro.')
    else:
        print(f'O número {resultado} é decimal.')
else:
    print('Opção de escolha inválida.')
