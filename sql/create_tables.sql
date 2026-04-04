CREATE TABLE dim_serie (
    id_serie SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    status VARCHAR(50),
    idioma_original VARCHAR(10),
    data_primeiro_ar DATE
);


CREATE TABLE dim_genero (
    id_genero SERIAL PRIMARY KEY,
    nome_genero VARCHAR(100)
);


CREATE TABLE dim_tempo (
    id_tempo SERIAL PRIMARY KEY,
    ano INT,
    mes INT,
    data_completa DATE
);



CREATE TABLE dim_temporada (
    id_temporada SERIAL PRIMARY KEY,
    numero_temporada INT,
    numero_episodios INT,
    data_lancamento DATE
);


CREATE TABLE fato_series (
    id_fato SERIAL PRIMARY KEY,

    id_serie INT,
    id_tempo INT,
    id_genero INT,
    id_temporada INT,

    avaliacao_media FLOAT,
    popularidade FLOAT,
    numero_votos INT,

    FOREIGN KEY (id_serie) REFERENCES dim_serie(id_serie),
    FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo),
    FOREIGN KEY (id_genero) REFERENCES dim_genero(id_genero),
    FOREIGN KEY (id_temporada) REFERENCES dim_temporada(id_temporada)
);

