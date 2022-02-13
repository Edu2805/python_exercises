"""
Criando um sistema de perguntas e respostas com
dicionários
"""

#Criando o dicionário e suas chaves

respostas_certas = 0
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas':{'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 3*2?',
        'respostas':{'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c',

    },
    'Pergunta 3':{
        'pergunta': 'Quanto é 1+2?',
        'respostas':{'a': '4', 'b': '3', 'c': '6'},
        'resposta_certa': 'b',

    },
    'Pergunta 4':{
        'pergunta': 'Quanto é 1-1?',
        'respostas':{'a': '0', 'b': '10', 'c': '6'},
        'resposta_certa': 'a',

    },
    'Pergunta 5':{
        'pergunta': 'Quanto é 8/4?',
        'respostas':{'a': '20', 'b': '1', 'c': '2'},
        'resposta_certa': 'c',

    }
}
print()
# inteirando sobre o dicionário
# acessando as chaves e valores
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
# acessando especificamente a chave resposta
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Resposta certa!')
        respostas_certas += 1
    else:
        print('resposta incorreta!')
    print()

qtd_perguntas = len(perguntas)
#quando os operadores possuem a mesma precedencia
#não há a necessidade de clocar parenteses
#a operacao é feita da esquerda para a direita
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} resposta(s).')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')