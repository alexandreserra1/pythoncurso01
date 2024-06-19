""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operacao = input('Digite a operação (+-/*): ')
    
    numeros_validos = None
    num_1_float =  0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os valores digitados são inválidos.')   
        continue
    
    operadores_permitidos = '+-/*'
    
    if operacao not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operacao) > 1:
        print('Digite apenas um operador.')
        continue
    
    
    if operacao == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operacao == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operacao == '*':
         print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    elif operacao == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
 
    else:
        print('Nunca deveria chegar aqui')
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
