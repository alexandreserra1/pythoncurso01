# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


respostas_certas = 0
for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")

    opcoes = pergunta['Opções']
    for opcao in opcoes:
        print(f'[{opcao}]: {opcao}')

    resposta = input("Sua resposta: ")
    if resposta == pergunta['Resposta']:
        print("Resposta correta!")
        respostas_certas += 1
    else:
        print("Resposta errada!")

    print()

print(f'Voce acertou {respostas_certas} respostas.')
print(f'Voce errou {len(perguntas) - respostas_certas} respostas.')
