import os
import time
import json
import pandas as pd
import logging
from selenium.webdriver.common.by import By
from automator.base_automator import BaseAutomator
from utils.validators import validar_aluno
from utils.sustainability import calcular_economia

logger = logging.getLogger(__name__)

class SigeAutomator(BaseAutomator):
    def __init__(self, excel_path, navegador='chrome', dry_run=False):
        super().__init__(navegador)
        self.excel_path = excel_path
        self.dry_run = dry_run
        self.resultados = []

        config_path = "automator/selectors.json"
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_path}")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def executar(self, usuario, senha):
        logger.info("Iniciando automação SIGE...")
        self.iniciar()
        self.driver.get(self.config['login_url'])

        # Login
        try:
            self.preencher(By.ID, self.config['login_fields']['usuario'], usuario)
            self.preencher(By.ID, self.config['login_fields']['senha'], senha)
            self.clicar(By.ID, self.config['login_fields']['botao'])
            logger.info("Login realizado com sucesso.")
        except Exception as e:
            logger.error(f"Falha no login: {e}")
            self.fechar()
            raise

        alunos = pd.read_excel(self.excel_path).to_dict(orient='records')
        logger.info(f"{len(alunos)} alunos carregados da planilha: {self.excel_path}")

        for aluno in alunos:
            inicio = time.time()
            try:
                erros = validar_aluno(aluno)
                if erros:
                    raise ValueError(f"Campos faltando: {', '.join(erros)}")

                if self.dry_run:
                    logger.info(f"[SIMULAÇÃO] {aluno['Nome']} processado.")
                else:
                    self._processar_aluno(aluno)

                status, msg = 'Sucesso', ''
            except Exception as e:
                status, msg = 'Erro', str(e)
                logger.error(f"Erro ao processar {aluno.get('Nome', 'Aluno desconhecido')}: {e}")
            finally:
                tempo = round(time.time() - inicio, 2)
                self.resultados.append({
                    'Nome': aluno.get('Nome'),
                    'Status': status,
                    'Mensagem': msg,
                    'Tempo': tempo
                })

        self._gerar_relatorio()
        folhas, co2 = calcular_economia(len(alunos))
        logger.info(f"Economia estimada: {folhas} folhas (~{co2} kg CO₂)")
        self.fechar()

    def _processar_aluno(self, aluno):
        pass

    def _gerar_relatorio(self):
        os.makedirs("relatorios", exist_ok=True)
        df = pd.DataFrame(self.resultados)
        caminho = "relatorios/relatorio_final.xlsx"
        df.to_excel(caminho, index=False)
        logger.info(f"Relatório gerado em: {caminho}")
