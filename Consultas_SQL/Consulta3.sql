SELECT s.nome, MAX(f.popularidade) AS popularidade
FROM fato_series f 
JOIN dim_serie s ON f.id_serie = s.id_serie
JOIN dim_tempo t ON f.id_tempo = t.id_tempo
WHERE t.ano = 2015 
GROUP BY s.nome 
ORDER BY popularidade DESC
LIMIT 1;