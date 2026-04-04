SELECT t.ano, AVG(f.avaliacao_media) AS media_avaliacao
FROM fato_series f
JOIN dim_serie s ON f.id_serie = s.id_serie
JOIN dim_tempo t ON f.id_tempo = t.id_tempo
WHERE s.nome = 'Better Call Saul'
GROUP BY t.ano
ORDER BY t.ano;