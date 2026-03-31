Projeto BI Data Warehouse: 

# Séries drama/criminal com API do TMDB  

# Primeira Fase do Projeto: 

<h2>

Aluno: Igor Alessandretti

<br>

Matrícula: 202839

<br>

Curso: Análise e Desenvolvimento de Sistemas 

</h2>

# Objetivo: 

<h2>

Construir um data warehouse a partir de dados reais de séries conectando com api do TMDB, aplicar conceitos de ETL para no final extrair as análises utilizando o PowerBI. 

</h2>


# 📈 Etapas do Projeto:

- <h2> 1. Modelagem do Data Warehouse </h2>

Inicialmente, foi realizado o desenho do modelo dimensional (Star Schema), definindo a tabela fato (fato_series) e as dimensões (dim_serie, dim_genero, dim_temporada e dim_tempo).

![](./modelagem_dimensional/modelagem_series.png)


- <h2> 2. Criação das tabelas no PostgreSQL  </h2>

As tabelas foram implementadas no banco de dados PostgreSQL com base no modelo definido, garantindo a estrutura necessária para análise.


# 📖 Dicionário de Dados: DW Séries

🧾 Tabela: fato_series

id_fato: Identificador único do registro da fato (Chave Primária).

id_serie: Chave estrangeira referenciando a dimensão de séries.

id_tempo: Chave estrangeira referenciando a dimensão de tempo.

id_genero: Chave estrangeira referenciando a dimensão de gênero.

id_temporada: Chave estrangeira referenciando a dimensão de temporada.

avaliacao_media: Nota média (0 a 10) atribuída à série ou temporada.

popularidade: Índice numérico de alcance e engajamento da produção.

numero_votos: Quantidade total de avaliações recebidas para o cálculo da média.


📋 Tabela: dim_serie


id_serie: Identificador único da série (Chave Primária).

nome: Título oficial da série.

status: Situação atual da obra (ex: "Returning Series", "Ended", "Canceled").

idioma_original: Sigla que representa o idioma de origem da produção.

data_primeiro_ar: Data de exibição do episódio piloto (estréia mundial).


📋 Tabela: dim_temporada
id_temporada: Identificador único da temporada (Chave Primária).

numero_temporada: Número sequencial que identifica a temporada (ex: 1, 2, 3).

numero_episodios: Quantidade de episódios contidos naquela temporada específica.

data_lancamento: Data oficial de lançamento da temporada.


📋 Tabela: dim_tempo
id_tempo: Identificador único da data (Chave Primária).

ano: Ano correspondente ao registro (formato AAAA).

mes: Mês correspondente ao registro (1 a 12).

data_completa: Data no formato completo (DD/MM/AAAA).


📋 Tabela: dim_genero
id_genero: Identificador único do gênero (Chave Primária).

nome_genero: Nome descritivo da categoria (ex: "Ação", "Documentário", "Drama").