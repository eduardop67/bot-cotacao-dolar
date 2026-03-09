import requests
from datetime import datetime
import json

def buscar_cotacao():
    resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
    if resposta.ok:
        dados = resposta.json()
        return float(dados['USDBRL']['bid'])
    else:
        return None

def salvar_historico(valor):
    try:
        with open("historico.json", "r", encoding="utf-8") as f:
            historico = json.load(f)
    except FileNotFoundError:
        historico = []
    
    registro = {
        "valor":valor,
        "data-hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    historico.append(registro)

    with open("historico.json", "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)

def verificar_alerta(cotacao_atual):
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            limite = config["limite"]
    except FileNotFoundError:
        limite = 5.5    
    if cotacao_atual > limite:
        print("AVISO cotacao atual maior que limite")
    


while True:
    print("=== BOT de cotacao === \n")
    print("[1] - ver cotacao atual \n")
    print("[2] - ver historico \n")
    print("[3] - verificar alerta\n")
    print("[4] - sair \n")
    escolha = input("digite sua escolha: ")
    if escolha == "1":
        cotacao = buscar_cotacao()
        salvar_historico(cotacao)
        print(f"COTACAO ATUAL: BRL {cotacao}")
    elif escolha == "2":
        try:
            with open("historico.json", "r", encoding="utf-8") as f:
                historico = json.load(f)
        except FileNotFoundError:
            historico = []
        if not historico:
            print("o historico esta vazio! ")
        else:
            for registro in historico:
                print(f"  R$ {registro['valor']:.2f}  —  {registro['data_hora']}")
    elif escolha == "3":
        cotacao = buscar_cotacao()
        verificar_alerta(cotacao)
    elif escolha == "4":
        break
    else:
        print("digite uma opcao valida")