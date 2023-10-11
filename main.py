from Biblioteca import *
while True:
    menu = input('Digite o número da operação que deseja realizar:\n1 Soma\n2 Subtração\n3 Multiplicação\n4 Divisão:\nS para Sair: ')

    x=int(input('Digite um número: '))
    y=int(input('Digite um número: '))

    if menu == '1':
        soma(x, y)
    elif menu == '2':
        subtrair(x,y)
    elif menu == '3':
        multiplicar(x,y)
    elif menu == '4':
        dividir(x,y)

    elif menu in 'Ss':
        break

print('Operação Finalizada!')



