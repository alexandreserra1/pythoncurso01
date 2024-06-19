"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero= input('Digite um numero inteiro:')
try:
    numero =int(numero)
    if numero % 2 == 0:
        print (f'o numero {numero} é par')
    else:
        print (f'o numero {numero} é impar')
except:
    print ('não é um numero inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print("Por favor, informe a hora atual sem os minutos.\nPor exemplo, se agora for 12:40, informe apenas 12.")
hora = input("Hora atual: ")
try:
  hora = int(hora)  
  if hora == 0 and hora <= 11:
      print("Bom dia!")
  elif hora > 11 and hora <= 17:
      print("Boa tarde!")
  else:
      print("Boa noite!")
except:
  print('Você não digitou a hora correta')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = input("Por favor, digite seu nome: ")

if nome.isalpha(): 
  try:
    if len(nome) <= 4:
      print("Seu nome é curto")
    elif len(nome) <= 6:
      print("Seu nome é normal")
    else:
      print("Seu nome é grande")
  except:
    print("Você não escreveu uma palavra")
else:
  print("Você digitou um nome inválido")
