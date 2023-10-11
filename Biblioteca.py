
def soma(n1, n2):
    resultado = n1 + n2
    print(resultado)

def subtrair(n1, n2):
    subtração = (n1 - n2)
    print(subtração)

def multiplicar(n1, n2):
    multiplicação = n1 * n2
    print(multiplicação)

def dividir(n1, n2):
    divisão = n1 / n2
    print(divisão)

def vogais(texto):
    cont = 0
    for x in texto:
        if x in 'aeiouAEIOU':
            cont+=1
    print(f'Quantidade de vogais {cont}')


def espaço(texto):
    cont = 0
    for x in texto:
        if x in ' ':
            cont+=1
    print(f'Quantidade de espaço {cont}')


def estoque (nome_produto,quan_prod_est,valor_unitário_prod):
    valor_total = quan_prod_est * valor_unitário_prod
    return valor_total


def imprimirmedia(nota1, nota2):
    media = (nota1 + nota2)/2
    return media


def situacao_do_aluno(nome, a):
    if a >= 7:
        return 'Aprovado', nome
    elif a >= 4:
        return 'Recuperação', nome
    else:
        return 'Reprovado', nome

def numero_interio (numero):
    if numero >0:
        return 'P'
    elif numero <0:
        return 'N'
    else:
        return 'Z'

def adicao (args):
    cont = 0
    for x in args:
        cont +=x
    return cont





