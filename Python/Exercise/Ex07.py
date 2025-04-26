print('Opçoes:')
print('1-[+]')
print('2-[-]')
print('3-[/]')
print('4-[*]')
escolha = float(input('Qual opção voce ira escolher?: '))
n1 = float(input('Qual o primeiro numero?: '))
n2 = float(input('Qual o segundo numero?: '))

if escolha == 1:
    print(f'O resultado da soma é: {n1+n2}')

elif escolha == 2:
    print(f'O resultado da subtração é: {n1-n2}')

elif escolha == 3:
    print(f'O resultado da divisão é: {n1/n2}')

elif escolha == 4:
    print(f'O resultado da multiplicação é: {n1*n2}')