from django.shortcuts import render
import requests
import json
from googletrans import Translator

# URL da API de Avatar
API_URL = "https://last-airbender-api.fly.dev/api/v1/characters"

def lista_personagens(request):
    """
    View responsável por consumir a API, traduzir e exibir os dados em um template.
    """
    try:
        # 1. CONSUMO DA API 
        response = requests.get(API_URL)
        response.raise_for_status() 
        
        personagens = response.json()
        
        # 2. TRADUÇÃO (Limitando a 10 para demonstração)
        translator = Translator()
        personagens_traduzidos = []
        
        for p in personagens[:10]:
            nome_original = p.get('name', 'N/A')
            
            try:
                # Se a afiliação for None, tratar como string vazia
                afiliacao_original = p.get('affiliation', '')
                
                nome_pt = translator.translate(nome_original, dest='pt').text
                afiliacao_pt = translator.translate(afiliacao_original, dest='pt').text if afiliacao_original else "Nenhuma/Desconhecida"
                
            except Exception:
                nome_pt = nome_original 
                afiliacao_pt = afiliacao_original

            
            personagens_traduzidos.append({
                'name': nome_pt,
                'affiliation': afiliacao_pt,
                'photoUrl': p.get('photoUrl', None),
            })

        # 3. ENVIO DOS DADOS PARA O TEMPLATE
        contexto = {
            'personagens': personagens_traduzidos
        }
        
        return render(request, 'personagens/lista.html', contexto)

    except requests.exceptions.RequestException as e:
        contexto = {
            'erro': f"Erro ao conectar ou buscar dados da API: {e}"
        }
        return render(request, 'personagens/erro.html', contexto, status=500)