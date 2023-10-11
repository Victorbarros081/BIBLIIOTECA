from Biblioteca import adicao

qtd = int(input('Quantos números? '))
v = [0]*qtd
for x in range (qtd):
    v[x]= float(input('Qual é o número? '))
w = adicao(v)
print(w)
