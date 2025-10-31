# ingest_s3.py
"""
Simulação de pipeline de ingestão de dados no Amazon S3.
Autor: Thiago Diniz
Objetivo: Demonstrar como um processo de ingestão seria estruturado em um ambiente de dados real.
"""

import os
import pandas as pd
from datetime import datetime

# Caminho local do arquivo CSV (dados simulados)
LOCAL_PATH = "data/raw/sample_data.csv"
# Nome do bucket simulado
S3_BUCKET = "s3://meu-bucket-exemplo"

def simulate_upload_to_s3(file_path, bucket):
    print(f"📦 Lendo arquivo: {file_path}")
    df = pd.read_csv(file_path)
    print(f"✅ Arquivo carregado com {len(df)} registros.")
    print(f"☁️ Simulando upload para bucket: {bucket}")
    print(f"🕒 Timestamp: {datetime.now()}")
    print("Upload concluído (simulação).")

if __name__ == "__main__":
    if os.path.exists(LOCAL_PATH):
        simulate_upload_to_s3(LOCAL_PATH, S3_BUCKET)
    else:
        print(f"❌ Arquivo não encontrado: {LOCAL_PATH}")
