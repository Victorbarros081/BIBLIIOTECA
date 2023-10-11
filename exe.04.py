'''Crie uma função que recebe o nome de um produto, a quantidade que tem no estoque o valor unitário
do produto. Retorne o valor total do meu estoque.'''

def estoque (nome_produto,quan_prod_est,valor_unitário_prod):
    valor_total = quan_prod_est * valor_unitário_prod
    return valor_total


valor_total = estoque('Feijão', 30, 4.50)

print(f'O valor total do estoque é {valor_total}')

