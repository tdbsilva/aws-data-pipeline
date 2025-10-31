-- redshift_schema.sql
-- Criação de tabela analítica para consumo no Redshift

CREATE TABLE analytics.performance_metrics (
    id INT,
    value DECIMAL(10,2),
    date DATE,
    value_adjusted DECIMAL(10,2),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
