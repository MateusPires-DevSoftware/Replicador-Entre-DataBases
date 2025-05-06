from db import get_connection

def replicar_dados(origem, destino):
    script_replicacao = f"""
    ADICIONE AQUI SEU SCRIPT
    """

    connections = get_connection("ORIGEM", "DESTINO")  
    conn_origem = connections.get("ORIGEM")
    conn_destino = connections.get("DESTINO")

    if conn_origem and conn_destino:
        try:
            cursor_destino = conn_destino.cursor()
            print(f"🚀 Iniciando replicação de {origem} para {destino}...")
            cursor_destino.execute(script_replicacao)
            conn_destino.commit()
            print(f"✅ Dados replicados com sucesso de {origem} para {destino}!")
        except Exception as e:
            print(f"❌ Erro na replicação: {e}")
        finally:
            conn_origem.close()
            conn_destino.close()
    else:
        print("❌ Falha ao conectar ao banco de dados.")
