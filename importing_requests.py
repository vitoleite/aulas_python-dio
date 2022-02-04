import requests

def retorna_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    print(response.status_code) # 200 significa que funcionou
    print(response.text) # imprime todo o texto da pagina, nesse caso o JSON
    dados_cep = response.json()
    return dados_cep['logradouro']

def retorna_site(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_site('https://www.google.com.br/')
    # print(response)
    print(retorna_cep('01001000'))
