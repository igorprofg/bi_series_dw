SELECT t.ano,t.mes, AVG(f.popularidade) AS popularidade
FROM fato_series f
JOIN dim_serie s ON f.id_serie = s.id_serie
JOIN dim_tempo t ON f.id_tempo = t.id_tempo
WHERE s.nome = 'Breaking Bad'
GROUP BY t.ano, t.mes
ORDER BY t.ano, t.mes;