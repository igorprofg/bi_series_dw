# Projeto BI Data Warehouse: 

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

<br>

# 📖 Dicionário de Dados: DW Séries

<br>

🧾 Tabela: fato_series

id_fato: Identificador único do registro da fato (Chave Primária).

id_serie: Chave estrangeira referenciando a dimensão de séries.

id_tempo: Chave estrangeira referenciando a dimensão de tempo.

id_genero: Chave estrangeira referenciando a dimensão de gênero.

id_temporada: Chave estrangeira referenciando a dimensão de temporada.

avaliacao_media: Nota média (0 a 10) atribuída à série ou temporada.

popularidade: Índice numérico de alcance e engajamento da produção.

numero_votos: Quantidade total de avaliações recebidas para o cálculo da média.

<br>

📋 Tabela: dim_serie


id_serie: Identificador único da série (Chave Primária).

nome: Título oficial da série.

status: Situação atual da obra (ex: "Returning Series", "Ended", "Canceled").

idioma_original: Sigla que representa o idioma de origem da produção.

data_primeiro_ar: Data de exibição do episódio piloto (estréia mundial).

<br>

📋 Tabela: dim_temporada
id_temporada: Identificador único da temporada (Chave Primária).

numero_temporada: Número sequencial que identifica a temporada (ex: 1, 2, 3).

numero_episodios: Quantidade de episódios contidos naquela temporada específica.

data_lancamento: Data oficial de lançamento da temporada.

<br>

📋 Tabela: dim_tempo
id_tempo: Identificador único da data (Chave Primária).

ano: Ano correspondente ao registro (formato AAAA).

mes: Mês correspondente ao registro (1 a 12).

data_completa: Data no formato completo (DD/MM/AAAA).

<br>

📋 Tabela: dim_genero
id_genero: Identificador único do gênero (Chave Primária).

nome_genero: Nome descritivo da categoria (ex: "Ação", "Documentário", "Drama").

<br>

# Segunda Fase do Projeto: 

<h1>O processo de ETL com os arquivos extract, transform e load encontra-se em:</h1>

# [ETL](./etl)

<br>

# Documentação: Pipeline ETL de Séries (TMDB API)


<h2>Extração (extract.py):</h2>

<h4>

Responsável por consumir os dados brutos da API externa.

Fonte: API do The Movie Database (TMDB).

Lógica: Realiza requisições paginadas (1 a 10) filtrando pelo gênero "Crime" (ID 80).

Saída: Salva os dados brutos em formato CSV em data/raw/series_raw.csv.

Segurança: Utiliza variáveis de ambiente (.env) para gerenciar a chave da API. </h4>

<h2> Transformação (transform.py): </h2>

<h4>

Nesta etapa, os dados brutos são limpos, normalizados e modelados seguindo o conceito de Star Schema (Esquema Estrela).

Limpeza: Converte strings de listas em objetos Python e trata duplicatas.

Modelagem Dimensional:

Dimensão Gênero (dim_genero): Mapeia IDs numéricos para nomes legíveis (ex: 80 -> Crime).

Dimensão Série (dim_serie): Armazena informações descritivas das séries (nome, idioma).

Dimensão Tempo (dim_tempo): Extrai granularidade de tempo (ano e mês) para análise temporal.

Fato Séries (fato_series): Tabela central com métricas quantitativas (popularidade, votos, média) e chaves estrangeiras para as dimensões.

Saída: Gera quatro arquivos CSV processados em data/processed/. </h4>

<h2>Carga (load.py):</h2>

<h4>

Responsável por persistir os dados transformados no data warehouse (PostgreSQL).

Conexão: Utiliza SQLAlchemy e psycopg2 para gerenciar o túnel de conexão com o banco.

Estratégia de Carga: Utiliza o método to_sql do Pandas com o parâmetro if_exists="append", permitindo o empilhamento de dados novos.

Segurança: Credenciais do banco (host, usuário, senha) são carregadas via variáveis de ambiente. </h4>


# OBS:

Alteração na Modelagem Dimensional

A dimensão dim_temporada foi inicialmente prevista na modelagem dimensional, porém não foi utilizada na implementação final do ETL.

Isso ocorreu porque os dados disponíveis no dataset não possuíam informações completas e consistentes sobre temporadas, como número da temporada, quantidade de episódios e datas específicas de lançamento por temporada.

Dessa forma, optou-se por não incluir essa dimensão no modelo físico, evitando inconsistências e mantendo a integridade das análises realizadas.
