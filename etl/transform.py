import pandas as pd
import ast

# =========================
# CARREGAR DADOS
# =========================

df = pd.read_csv("data/processed/series_clean.csv")

# converter string para lista
df["genre_ids"] = df["genre_ids"].apply(ast.literal_eval)

# =========================
# DIM GENERO
# =========================

generos_map = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western",
    10759: "Action & Adventure",
    10762: "Kids",
    10763: "News",
    10764: "Reality",
    10765: "Sci-Fi & Fantasy",
    10766: "Soap",
    10767: "Talk",
    10768: "War & Politics"
}

df_genero = df[["genre_ids"]].explode("genre_ids")
df_genero = df_genero.drop_duplicates(subset=["genre_ids"])
df_genero = df_genero.rename(columns={"genre_ids": "id_genero"})
df_genero["nome_genero"] = df_genero["id_genero"].map(generos_map)

df_genero.to_csv("data/processed/dim_genero.csv", index=False)

# =========================
# DIM SERIE
# =========================

df_serie = df[[
    "id",
    "name",
    "original_language"
]].drop_duplicates()

df_serie = df_serie.rename(columns={
    "id": "id_serie",
    "name": "nome",
    "original_language": "idioma_original"
})

df_serie.to_csv("data/processed/dim_serie.csv", index=False)

# =========================
# DIM TEMPO
# =========================

df_tempo = df[["ano", "mes"]].drop_duplicates().reset_index(drop=True)

df_tempo["id_tempo"] = df_tempo.index + 1

df_tempo.to_csv("data/processed/dim_tempo.csv", index=False)

# =========================
# FATO SERIES
# =========================

df_fato = df.copy()

# explode gênero
df_fato = df_fato.explode("genre_ids")

df_fato = df_fato.rename(columns={
    "id": "id_serie",
    "genre_ids": "id_genero",
    "vote_average": "avaliacao_media",
    "popularity": "popularidade",
    "vote_count": "numero_votos"
})

# relacionar com dim_tempo
df_fato = df_fato.merge(df_tempo, on=["ano", "mes"], how="left")

# selecionar apenas colunas corretas
df_fato = df_fato[[
    "id_serie",
    "id_genero",
    "id_tempo",
    "avaliacao_media",
    "popularidade",
    "numero_votos"
]]

df_fato.to_csv("data/processed/fato_series.csv", index=False)

print("Arquivos gerados com sucesso!")