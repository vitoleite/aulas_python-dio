class Calculadora():
    def __init__(self, num1, num2):
        # init será o iniciável da classe, isso quer dizer que outras funcoes nao necessariamente precisarão ter
        # valores para declarar, isso se utilizar a funcao dentro da classe.
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
