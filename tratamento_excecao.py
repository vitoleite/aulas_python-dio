# Hierarquia de retorno para erros, sendo que Base Exception é o primeiro.

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, mensagem):
        self.mensagem = mensagem


while True:
    try:
        x = int(input('Número de 1 a 10: '))
        if x > 10: raise InputError('número maior que 10')
        elif x < 1: raise InputError('número menor que 1')
    except Exception as ex:
        print(f'Erro, mais específico: {ex}')
    else:
        # Executa quando não ocorre exceção
        print(x)
        break
