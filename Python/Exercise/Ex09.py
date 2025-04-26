print('opções:')
print('1-[dollar]')
print('2-[real]')
escolha = float(input('Qual moeda você quer converter?: '))
valor = float(input('Qual o valor?: '))

if escolha == 1:
    print(f'O resultado em reais fica: {valor * 5.6}')

elif escolha == 2:
    print(f'O resultado em dolares fica: {valor / 5.6}')