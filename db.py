# db.py
import pyodbc
import config

def get_connection(origem, destino):
    """Estabelece conexão com as bases ORIGEM e DESTINO"""
    connections = {}

    for key in [origem, destino]:
        db_config = config.DATABASES.get(key)

        if not db_config:
            print(f"Opção inválida! Base '{key}' não encontrada no config.")
            connections[key] = None
            continue

        try:
            conn = pyodbc.connect(
                f"DRIVER={db_config['DRIVER']};"
                f"SERVER={db_config['SERVER']};"
                f"DATABASE={db_config['NAME']};"
                f"UID={db_config['USERNAME']};"
                f"PWD={db_config['PASSWORD']}"
            )
            print(f"✅ Conectado à base: {db_config['NAME']}")
            connections[key] = conn
        except Exception as e:
            print(f"❌ Erro ao conectar à base {key}: {e}")
            connections[key] = None

    return connections
