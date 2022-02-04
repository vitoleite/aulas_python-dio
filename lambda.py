# lambda (parametro) : retorno
# lambda é uma especie de função anonima

contador = lambda lista: [len(s) for s in lista]
lista_animais = ['cachorro', 'gato', 'urubu']
print(contador(lista_animais))

soma = lambda a, b: a + b
print(soma(5, 10))

calculator = {
    'sum': lambda a, b: a + b,
    'subtraction': lambda a, b: a - b,
    'multiplicacao': lambda  a, b: a * b
}

soma = calculator['sum']
print(soma(1, 2))