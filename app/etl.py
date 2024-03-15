import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine
import pandera as pa
from schema import MyDataFrameSchema

def load_settings():
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host" : os.getenv("POSTGRES_HOST"),
        "db_user" : os.getenv("POSTGRES_USER"),
        "db_pass" : os.getenv("POSTGRES_PASSWORD"),
        "db_name" : os.getenv("POSTGRES_DB"),
        "db_port" : os.getenv("POSTGRES_PORT"),        
    }
    return settings

# pa.check_output(MyDataFrameSchema)

@pa.check_output(MyDataFrameSchema, lazy=True)
def extrair_do_sql(query: str) -> pd.DataFrame:

    settings = load_settings()
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
        df = pd.read_sql(query, conn)

    return df

if __name__ == "__main__":
    query = "select * from produtos_bronze_email"
    df = extrair_do_sql(query=query)
    print(df)


# Cria a URL de conexao com o banco de dados
# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"