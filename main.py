import pyodbc
import os
from functions import replicar_dados

# Configurações de conexão - Defina o servidor e credenciais
#SQL_SERVER = "SRV-SQLSERVER2\\MSSQLSERVER2017"
#USERNAME = "itprovider"
#PASSWORD = "passitpxyz"
#DRIVER = "ODBC Driver 17 for SQL Server"
SQL_SERVER = input("Informe o SQL Server (ex: SRV-SQLSERVER2\\MSSQLSERVER2017): ").strip()
USERNAME = input("Informe o usuário do SQL Server: ").strip()
PASSWORD = input("Informe a senha do SQL Server: ").strip()
DRIVER = "ODBC Driver 17 for SQL Server"

def conectar_e_listar_bases():
    """Conecta ao SQL Server e lista todas as bases disponíveis"""
    try:
        conn = pyodbc.connect(
            f"DRIVER={DRIVER};SERVER={SQL_SERVER};UID={USERNAME};PWD={PASSWORD}"
        )
        cursor = conn.cursor()


        cursor.execute("SELECT name FROM sys.databases WHERE state_desc = 'ONLINE';")
        bases = [db[0] for db in cursor.fetchall()]

        cursor.close()
        conn.close()


        print("\nBases de dados disponíveis:")
        for i, base in enumerate(bases, 1):
            print(f"{i}. {base}")

        return bases

    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        return []

def escolher_base(mensagem, bases, escolhida_anteriormente=None):
    """Permite ao usuário escolher uma base de dados"""
    while True:
        try:
            escolha = int(input(f"\n{mensagem}: ")) - 1

            if escolha < 0 or escolha >= len(bases):
                print("Número inválido! Escolha novamente.")
                continue

            if escolhida_anteriormente and bases[escolha] == escolhida_anteriormente:
                print("Você já escolheu essa base! Escolha outra.")
                continue

            return bases[escolha]
        except ValueError:
            print("Entrada inválida! Digite um número.")

def salvar_config(base_origem, base_destino):
    """Salva as bases escolhidas no arquivo config.py"""
    config_content = f"""# config.py

DATABASES = {{
    "ORIGEM": {{
        "NAME": "{base_origem}",
        "SERVER": "{SQL_SERVER}",
        "USERNAME": "{USERNAME}",
        "PASSWORD": "{PASSWORD}",
        "DRIVER": "{DRIVER}"
    }},
    "DESTINO": {{
        "NAME": "{base_destino}",
        "SERVER": "{SQL_SERVER}",
        "USERNAME": "{USERNAME}",
        "PASSWORD": "{PASSWORD}",
        "DRIVER": "{DRIVER}"
    }}
}}
"""

    with open("config.py", "w") as f:
        f.write(config_content)

    print("\nConfigurações salvas em config.py!")

if __name__ == "__main__":
    bases_disponiveis = conectar_e_listar_bases()

    if bases_disponiveis:
        base_origem = escolher_base("Escolha a base ORIGEM", bases_disponiveis)
        base_destino = escolher_base("Escolha a base DESTINO", bases_disponiveis, escolhida_anteriormente=base_origem)

       
        print("\nBases selecionadas:")
        print(f"🔹 Base Origem: {base_origem}")
        print(f"🔹 Base Destino: {base_destino}")

        salvar_config(base_origem, base_destino)

        replicar_dados(base_origem, base_destino)

    else:
        print("Nenhuma base de dados disponível ou erro na conexão.")
