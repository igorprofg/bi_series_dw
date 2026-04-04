import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# conexão com PostgreSQL
# Carrega as variáveis do arquivo .env
load_dotenv()

# Puxa os dados das variáveis de ambiente
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

# Monta a URL de conexão de forma segura 
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# CARREGAR CSVs

df_serie = pd.read_csv("data/processed/dim_serie.csv")
df_genero = pd.read_csv("data/processed/dim_genero.csv")
df_tempo = pd.read_csv("data/processed/dim_tempo.csv")
df_fato = pd.read_csv("data/processed/fato_series.csv")

# ENVIAR PARA O BANCO

df_serie.to_sql("dim_serie", engine, if_exists="append", index=False)
df_genero.to_sql("dim_genero", engine, if_exists="append", index=False)
df_tempo.to_sql("dim_tempo", engine, if_exists="append", index=False)
df_fato.to_sql("fato_series", engine, if_exists="append", index=False)

print("Dados carregados no PostgreSQL com sucesso!")