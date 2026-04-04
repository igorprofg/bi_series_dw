SELECT s.nome, MAX(f.popularidade) AS popularidade
FROM fato_series f
JOIN dim_serie s ON f.id_serie = s.id_serie
WHERE s.nome = 'Peaky Blinders'
GROUP BY s.nome;