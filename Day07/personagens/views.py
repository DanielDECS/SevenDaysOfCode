import requests
from googletrans import Translator
from django.shortcuts import render
# Importa as classes necessárias para a paginação
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

def lista_personagens(request):
    try:
        # 1. Consumo da API e Preparação dos Dados
        # Aumentei o perPage para 50 para garantir dados suficientes para a paginação.
        url = 'https://last-airbender-api.fly.dev/api/v1/characters?perPage=50' 
        response = requests.get(url)
        # Lança exceção para status HTTP de erro (4xx ou 5xx)
        response.raise_for_status() 
        personagens_data = response.json()
        
        translator = Translator()
        personagens_traduzidos = []

        # 2. Lógica de Tradução e Filtro (dos Dias anteriores)
        for p in personagens_data:
            # Pula personagens sem nome ou que sejam 'Unknown'
            if not p.get('name') or p.get('name').lower() == 'unknown':
                continue

            nome_traduzido = translator.translate(p.get('name', 'Nome Desconhecido'), src='en', dest='pt').text
            
            afiliacao = p.get('affiliation', 'Unknown')
            # Traduz a afiliação, se existir e não for 'Unknown'
            if afiliacao and afiliacao.lower() != 'unknown':
                 afiliacao_traduzida = translator.translate(afiliacao, src='en', dest='pt').text
            else:
                afiliacao_traduzida = 'Desconhecida'


            personagens_traduzidos.append({
                'name': nome_traduzido,
                'affiliation': afiliacao_traduzida,
                'photoUrl': p.get('photoUrl', ''),
            })
            
        # 3. Lógica de Paginação
        
        # Define quantos itens serão exibidos por página
        itens_por_pagina = 10 
        
        # Cria o objeto Paginator com a lista de todos os dados e o número de itens por página
        paginator = Paginator(personagens_traduzidos, itens_por_pagina)
        
        # Obtém o número da página a partir do parâmetro 'page' na URL (ex: /?page=2)
        page_number = request.GET.get('page')
        
        try:
            # Obtém o objeto Page (a fatia de dados) correspondente ao número da página
            personagens_paginados = paginator.get_page(page_number)
        except PageNotAnInteger:
            # Se o 'page' não for um número (ou estiver ausente), exibe a primeira página
            personagens_paginados = paginator.page(1)
        except EmptyPage:
            # Se o 'page' estiver fora do intervalo (ex: pedindo a página 10 de 5), exibe a última página
            personagens_paginados = paginator.page(paginator.num_pages) 
        
        contexto = {
            # Passamos o objeto Page, que será iterado no template
            'personagens': personagens_paginados, 
            'erro': None
        }

    except requests.exceptions.RequestException as e:
        contexto = {'personagens': [], 'erro': f"Erro ao acessar a API: {e}"}
    except Exception as e:
        # Captura outros erros, como de tradução ou JSON malformado
        contexto = {'personagens': [], 'erro': f"Ocorreu um erro interno: {e}"}

    return render(request, 'personagens/lista.html', contexto)