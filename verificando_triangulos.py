print('---------------------------------------------------------')
print('               VERIFICANDO TRIÂNGULOS                    ')
print('---------------------------------------------------------')

lado1 = float(input('Digite o valor do primeiro lado do triângulo: '))
lado2 = float(input('Digite o valor do segundo lado do triângulo: '))
lado3 = float(input('Digite o valor do terceiro lado do triângulo: '))

if(lado1 and lado2 and lado3 > 0):
    if(lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2):
        if(lado1 == lado2 == lado3):
            print('O triângulo é equilátero.')
        elif(lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1):
            print('O triângulo é isósceles.')
        else:
            print('O triângulo é escaleno.')
    else:
        print('O triângulo não pode ser formado.')
else:
    print('As opções dos lados são inválidas.')
