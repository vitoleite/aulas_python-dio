class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, mensagem):
        self.mensagem = mensagem


while True:
    try:
        nota = int(input('Digite uma nota de 0 a 10: '))
        #print(nota)
        if nota > 10:
            # Raise força a mostrar uma exceção
            raise InputError('Nota maior que 10.')
        elif nota < 0:
            raise InputError('Nota menor que 0.')
    except ValueError:
        print('Valor inválido.')
    except InputError as ex:
        print(ex)
    else:
        print(f'A sua nota foi: {nota}')
        break