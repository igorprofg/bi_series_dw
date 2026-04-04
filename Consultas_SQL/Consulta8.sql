SELECT s.nome, MIN(t.ano) AS ano_inicio, AVG(f.popularidade) AS media_popularidade
FROM fato_series f
JOIN dim_serie s ON f.id_serie = s.id_serie
JOIN dim_tempo t ON f.id_tempo = t.id_tempo
GROUP BY s.nome
HAVING MIN(t.ano) <= 2010
ORDER BY media_popularidade DESC
LIMIT 10;