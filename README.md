# OpenAI Chat Completion Example

Este projeto é um exemplo de como usar a API do OpenAI para obter uma conclusão de chat com o modelo GPT-4. A aplicação carrega a chave da API do OpenAI a partir de variáveis de ambiente e faz uma solicitação para obter uma resposta.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python: `openai`, `python-dotenv`

## Configuração

1. **Clone o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_SEU_REPOSITORIO>
    ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Crie um arquivo `.env` na raiz do projeto e adicione a chave da API do OpenAI:**

    ```plaintext
    OPENAI_API_KEY=Sua_Chave_Aqui
    ```

    **Nota:** Substitua `Sua_Chave_Aqui` pela sua chave real da API do OpenAI.

## Execução

Para executar o script e obter uma conclusão de chat, use o comando:

```bash
python main.py
