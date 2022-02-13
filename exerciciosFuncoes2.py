def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):# argumentos recebem diversis tipos
    return funcao()

executando = mestre(ola_mundo)
print(executando)

################################

def mestre1(funcao1, *args, **kwargs):
    return funcao1(*args, **kwargs)

def fala_oi(nome1):
    return f'Oi {nome1}'

def saudacao (nome1, saudacao):
    return f'{saudacao} {nome1}'

executando1 = mestre1(fala_oi, 'Luiz')
executando2 = mestre1(saudacao, 'Luiz', saudacao='Bom dia')
print(executando1)
print(executando2)
