def funcao_a():
    print("Início da função A")
    funcao_b()
    print("Fim da função A")

def funcao_b():
    print("Início da função B")
    funcao_c()
    print("Fim da função B")

def funcao_c():
    print("Início da função C")
    print("Fim da função C")

funcao_a()
