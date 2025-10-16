# Dia 2 - Um script que primeiro reutiliza o código de consumo da API do Dia 1 e depois aplica a tradução.

import requests                    # Biblioteca para fazer requisições HTTP
from googletrans import Translator # Biblioteca para tradução de texto
import pprint                      # Biblioteca para imprimir dados de forma legível

# --- Configurações ---
API_URL = "https://last-airbender-api.fly.dev/api/v1/characters"
TRADUTOR = Translator()

def obter_personagens():
    """Consome a API de Avatar e retorna a lista de personagens (JSON como lista Python)."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao obter dados da API: {e}")
        return None

def traduzir_atributos(personagens):
    """
    Traduz os atributos 'name' e 'affiliation' de uma lista de personagens.
    
    A API retorna os nomes e afiliações em Inglês, vamos traduzir para Português (pt).
    """
    personagens_traduzidos = []
    
    # 1. Passar uma função para ler os nomes e afiliações
    for personagem in personagens:
        # Pega os valores atuais (em Inglês, assumidamente)
        nome_original = personagem.get('name', 'N/A')
        afiliacao_original = personagem.get('affiliation', 'N/A')
        
        # 2. Traduzir esses atributos
        
        # Traduz o nome
        try:
            nome_traduzido = TRADUTOR.translate(nome_original, dest='pt').text
        except Exception:
            nome_traduzido = nome_original + " (Erro Trad.)"
        
        # Traduz a afiliação (e garante que não é None)
        if afiliacao_original and afiliacao_original != 'N/A':
             try:
                afiliacao_traduzida = TRADUTOR.translate(afiliacao_original, dest='pt').text
             except Exception:
                 afiliacao_traduzida = afiliacao_original + " (Erro Trad.)"
        else:
            afiliacao_traduzida = "Nenhuma/Desconhecida"

        # Cria uma cópia do personagem com os novos atributos (ou adiciona novos campos)
        personagem_traduzido = personagem.copy()
        
        # Armazena as traduções (você pode decidir se quer sobrescrever ou criar novos campos)
        personagem_traduzido['name_pt'] = nome_traduzido
        personagem_traduzido['affiliation_pt'] = afiliacao_traduzida
        
        personagens_traduzidos.append(personagem_traduzido)
        
    return personagens_traduzidos

if __name__ == "__main__":
    
    # Obter os dados brutos
    dados_personagens = obter_personagens()
    
    if dados_personagens:
        
        # Traduzir apenas os primeiros 5 para a demonstração (a lista completa é grande!)
        personagens_para_traduzir = dados_personagens[:5] 
        
        # Chamar a função de tradução
        dados_traduzidos = traduzir_atributos(personagens_para_traduzir)
        
        # 3. Imprimir os nomes traduzidos
        print("\n--- Exibição dos Primeiros 5 Personagens Traduzidos (name_pt e affiliation_pt) ---")
        for p in dados_traduzidos:
            print(f"Nome Original: {p.get('name', 'N/A'):<30} | Nome PT: {p.get('name_pt', 'N/A')}")
            print(f"Afili. Original: {p.get('affiliation', 'N/A'):<30} | Afili. PT: {p.get('affiliation_pt', 'N/A')}\n")
            
        print("\n--- Estrutura Completa de um Personagem Traduzido (Exemplo) ---")
        pprint.pprint(dados_traduzidos[0])