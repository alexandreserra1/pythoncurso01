def multiplicar(*args):
    total =  1
    for numero in args:
        total *= numero
    return total


print(multiplicar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))


def somar(*args):
    return sum(args)

print(somar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def par_impar(*args):
    return 'par' if sum(args) % 2 == 0 else 'impar'

print(par_impar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
