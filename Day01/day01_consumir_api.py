# Dia 01 - Um script para consumir uma API pública e imprimir a resposta JSON.
# API utilizada: Personagens de Avatar (https://last-airbender-api.fly.dev/)

import requests # Biblioteca para fazer requisições HTTP
import json     # Biblioteca para manipular dados em formato JSON
import pprint   # Biblioteca para imprimir dados de forma legível

# URL da API de personagens de Avatar
API_URL = "https://last-airbender-api.fly.dev/api/v1/characters"

# Função para consumir a API e imprimir a resposta
def consumir_api_avatar():
    """
    Realiza uma requisição GET para a API de personagens de Avatar e imprime a resposta.
    """



    print(f"1. Fazendo requisição GET para a API: {API_URL}")
    try:
        # 1. Criar o código Python para executar uma requisição HTTP do tipo GET
        response = requests.get(API_URL)
        # Garante que a requisição foi bem-sucedida (código de status 200)
        response.raise_for_status()
        # 2. Executar a requisição e pegar a resposta (o JSON)
        # O método .json() do requests converte o corpo da resposta em um objeto Python (lista/dicionário)
        data = response.json()
        # 3. Imprimir o corpo da resposta (JSON)
        print("\n2. Resposta JSON completa (corpo da resposta):")
        # Usando o pprint para formatar o JSON de forma mais organizada na saída
        pprint.pprint(data)
        print("\n3. Outra forma de imprimir o JSON formatado):")
        print(json.dumps(data, indent=4))  
        # Imprime o número total de personagens recebidos, apenas como verificação extra
        print(f"\nTotal de personagens recebidos: {len(data)}")
    
    except requests.exceptions.RequestException as e:
        print(f"\n[ERRO] Não foi possível conectar à API ou a requisição falhou: {e}")

# “Só execute consumir_api_avatar() se este arquivo for rodado diretamente e não quando ele for importado por outro código.”
if __name__ == "__main__":
    consumir_api_avatar()