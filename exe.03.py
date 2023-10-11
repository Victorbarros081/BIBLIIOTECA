def espaço(texto):
    cont = 0
    for x in texto:
        if x in ' ':
            cont+=1
    print(f'Quantidade de espaço {cont}')

espaço('o rato roeu a roupa do rei de roma')

