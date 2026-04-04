SELECT g.nome_genero, COUNT(*) AS total
FROM fato_series f
JOIN dim_genero g ON f.id_genero = g.id_genero
GROUP BY g.nome_genero
ORDER BY total DESC;