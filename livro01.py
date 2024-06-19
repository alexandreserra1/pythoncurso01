#escreva o codigo para a funncao soma, vista anteriormennte
#escreva umna funncao recursiva que conte o numero de itens em uma lista
#encontre o valor mais alto em umna lista


def soma(x, y):
    return x + y
print(soma(2, 3))

def soma_recursiva(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + soma_recursiva(lista[1:])
print(soma_recursiva([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



