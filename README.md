# Desafio #7DaysOfCode - Python Web 🐍🌐

Este repositório contém os projetos desenvolvidos durante o desafio **7 Days of Code - Python Web**, uma iniciativa da Alura. O objetivo é exercitar e aprofundar conhecimentos em desenvolvimento web utilizando a linguagem Python.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Django
* **Estilização:** Bootstrap
* **Outras Bibliotecas:** `requests`, `googletrans` (versão 3.1.0a0)g

---

## 📅 Estrutura do Desafio

### Dia 1: Configuração Inicial e Consumo de API

**Tarefa:** Consumir a API de personagens do Avatar (`https://last-airbender-api.fly.dev/api/v1/characters`) usando a biblioteca `requests`, e imprimir a resposta JSON no console.

**Status:** ✅ Concluído

### Dia 2: Manipulação de Dados e Tradução de Atributos

**Tarefa:** Fazer a tradução dos atributos `name` e `affiliation` dos personagens usando a biblioteca `googletrans` e imprimir os resultados traduzidos.

**Status:** ✅ Concluído

### Dia 3: Configuração do Projeto Django

**Tarefa:** Iniciar um projeto Django e um aplicativo (`personagens`), fazer as configurações necessárias para registro do app e executar o projeto com sucesso. (O projeto Django foi iniciado na pasta `Day03`).

**Status:** ✅ Concluído

### Dia 4: Criação de Views, Rotas e Templates

**Tarefa:** Criar a View (lógica), configurar as rotas (`urls.py`) do projeto e do app, e usar um template HTML simples para exibir os dados dos personagens consumidos e traduzidos da API. (O trabalho foi desenvolvido na pasta `Day04`).

**Status:** ✅ Concluído

### Dia 5: Estilização com Bootstrap e Tabela de Dados

**Tarefa:** Integrar o framework Bootstrap ao template e desenvolver uma tabela HTML estilizada para organizar e exibir de forma clara os dados (foto, nome e afiliação) dos personagens consumidos da API. (O trabalho foi desenvolvido na pasta `Day05`).

**Status:** ✅ Concluído

### Dia 6: Geração de ID Sequencial com Template Tags

**Tarefa:** Implementar uma coluna de ID sequencial na tabela, utilizando a template tag `forloop.counter` do Django para gerar um número fixo para cada item, simulando um ID automático na visualização. (O trabalho foi desenvolvido na pasta `Day06`).

**Status:** ✅ Concluído

### Dia 7: Paginação dos Dados

**Tarefa:** Implementar a lógica de paginação na view, utilizando o utilitário `Paginator` do Django para dividir a lista de personagens em páginas menores, melhorando a performance e a experiência do usuário. (O trabalho foi desenvolvido na pasta `Day07`).

**Status:** 🎉 Concluído

---

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/DanielDECS/SevenDaysOfCodePython.git](https://github.com/DanielDECS/SevenDaysOfCodePython.git)
    cd SevenDaysOfCodePython
    ```

2.  **Crie e ative um ambiente virtual:**
    * *Nota: Se encontrar erros de compatibilidade, use o Python 3.12 (ou anterior) para criar o venv.*
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    .\venv\Scripts\activate    # No Windows (Command Prompt)
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação (a partir da pasta `Day07`):**
    ```bash
    cd Day07
    python manage.py runserver
    ```
    
5.  **Acesse:**
    Abra seu navegador e acesse `http://127.0.0.1:8000/`.

---

## 👤 Autor

* **Daniel Soares**
    * **GitHub:** https://github.com/DanielDECS
    * **LinkedIn:** https://www.linkedin.com/in/danieldecs/