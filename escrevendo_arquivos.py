# arq = open('arquivo.txt', 'w')

def escrever(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    escrever("notas.txt", 'Vitor,5,10,7,6')
    #atualizar("yes, you're cool")
    #ler('notas.txt')