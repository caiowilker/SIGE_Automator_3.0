import os
import pandas as pd
import sqlite3
import logging
from data.word_importer import extract_from_word, export_to_excel

logger = logging.getLogger(__name__)

class DataManager:
    def __init__(self, source='excel', path='data/alunos_modelo.xlsx'):
        self.source = source
        self.path = path

    def carregar_dados(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Arquivo de dados não encontrado: {self.path}")

        logger.info(f"Carregando dados a partir de: {self.source} ({self.path})")

        if self.source == 'excel':
            df = pd.read_excel(self.path)
            return df.to_dict(orient='records')

        elif self.source == 'sqlite':
            conn = sqlite3.connect(self.path)
            df = pd.read_sql_query("SELECT * FROM alunos", conn)
            conn.close()
            return df.to_dict(orient='records')

        else:
            raise ValueError("Fonte de dados não suportada. Use 'excel' ou 'sqlite'.")

    @staticmethod
    def importar_dados_word(caminho_docx: str):
        df = extract_from_word(caminho_docx)
        excel_path = export_to_excel(df)
        return excel_path

    def salvar_no_banco(self, df: pd.DataFrame, tabela="alunos"):
        os.makedirs("data/db", exist_ok=True)
        db_path = "data/db/alunos.db"
        conn = sqlite3.connect(db_path)
        df.to_sql(tabela, conn, if_exists='append', index=False)
        conn.close()
        logger.info(f"Dados salvos no banco SQLite: {db_path} (tabela {tabela})")
