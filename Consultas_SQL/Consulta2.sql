SELECT s.nome, AVG(f.avaliacao_media) AS media_avaliacao
FROM fato_series f 
JOIN dim_serie s ON f.id_serie = s.id_serie
GROUP BY s.nome
ORDER BY media_avaliacao DESC 
LIMIT 10; 