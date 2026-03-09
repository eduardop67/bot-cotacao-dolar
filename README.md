# Bot de Cotação do Dólar

Aplicação de terminal que busca a cotação atual do dólar, 
salva o histórico de consultas e emite alertas quando o valor 
ultrapassa um limite configurado.

## Funcionalidades

- Cotação em tempo real via AwesomeAPI
- Histórico de consultas salvo em JSON
- Sistema de alerta configurável
- Menu interativo no terminal

## Tecnologias

- Python 3.x
- requests
- json
- datetime

## Como rodar

# 1. Clone o repositório
git clone https://github.com/seu-usuario/bot-cotacao-dolar

# 2. Entre na pasta
cd bot-cotacao-dolar

# 3. Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Rode o programa
python main.py

## Configurando o limite de alerta

Crie um arquivo `config.json` na raiz do projeto:
{
    "limite": 5.50
}
Se o arquivo não existir, o limite padrão é R$ 5,50.

## Estrutura do projeto

bot-cotacao-dolar/
├── main.py
├── config.json
├── historico.json  ← gerado automaticamente
├── requirements.txt
└── README.md