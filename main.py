import time
import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave da API da variável de ambiente
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

# Verifica se a chave da API foi carregada corretamente
if OPENAI_KEY is None:
    raise ValueError("A chave da API do OpenAI não foi encontrada. Verifique o arquivo .env.")

# Define a chave da API para o cliente OpenAI
openai.api_key = OPENAI_KEY

def get_chat_completion():
    try:
        # Cria uma solicitação de conclusão de chat
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """
                    Você é um assistente que entrega manuais de manutenção de aparelhos eletrônicos de acordo
                    com o que o funcionário/cliente deseja.
                    Você deve retornar apenas um breve detalhe sobre o manual e um link de algum site 
                    que possa fornecer o devido manual ou para acesso.
                """},
                {"role": "user", "content": "Olá!"}
            ]
        )
        # Imprime o conteúdo da mensagem de resposta
        response_content = completion.choices[0].message['content']
        print(response_content)
    except openai.error.RateLimitError as e:
        print(f"Erro de limite de taxa: {e}")
        # Atraso antes de tentar novamente
        time.sleep(60)  # Aguarda 60 segundos
        get_chat_completion()
    except openai.error.OpenAIError as e:
        # Captura outros erros da API do OpenAI
        print(f"Erro na API do OpenAI: {e}")
    except Exception as e:
        # Captura quaisquer outros erros inesperados
        print(f"Erro inesperado: {e}")

# Chama a função para obter a conclusão do chat
get_chat_completion()
