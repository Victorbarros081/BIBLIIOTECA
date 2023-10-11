from Biblioteca import imprimirmedia
from Biblioteca import situacao_do_aluno

nome = input('Nome do Aluno: ')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a primeira nota: '))

x = imprimirmedia(nota1, nota2)
y = situacao_do_aluno(nome,x)

print(f'O aluno {y[1]}, está {y[0]}!')

