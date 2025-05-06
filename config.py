# config.py

DATABASES = {
    "ORIGEM": {
        "NAME": "INTEGRACAO_BDS",
        "SERVER": "SRV-SQLSERVER2\MSSQLSERVER2017",
        "USERNAME": "USER",
        "PASSWORD": "SENHAUSER",
        "DRIVER": "ODBC Driver 17 for SQL Server"
    },
    "DESTINO": {
        "NAME": "AGMBCK_COMERCIAL",
        "SERVER": "SRV-SQLSERVER2\MSSQLSERVER2017",
        "USERNAME": "USERr",
        "PASSWORD": "SENHAUSER",
        "DRIVER": "ODBC Driver 17 for SQL Server"
    }
}
