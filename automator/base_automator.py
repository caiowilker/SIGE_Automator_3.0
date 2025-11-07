import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger(__name__)

class BaseAutomator:
    def __init__(self, navegador='chrome', timeout=15):
        self.navegador = navegador
        self.driver = None
        self.timeout = timeout

    def iniciar(self):
        if self.navegador == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            self.driver = webdriver.Chrome(options=options)

        elif self.navegador == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Edge(options=options)

        else:
            raise ValueError("Navegador não suportado.")

        logger.info(f"Navegador iniciado: {self.navegador}")

    def esperar(self, by, valor):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, valor))
            )
        except TimeoutException as e:
            logger.error(f"Timeout ao esperar elemento: {valor}")
            raise e

    def clicar(self, by, valor):
        try:
            elemento = self.esperar(by, valor)
            elemento.click()
            logger.info(f"Clique realizado em: {valor}")
        except Exception as e:
            logger.error(f"Erro ao clicar em {valor}: {e}")
            self.capturar_print("erro_clicar.png")
            raise

    def preencher(self, by, valor, texto):
        try:
            campo = self.esperar(by, valor)
            campo.clear()
            campo.send_keys(texto)
            logger.info(f"Campo preenchido: {valor} -> {texto}")
        except Exception as e:
            logger.error(f"Erro ao preencher {valor}: {e}")
            self.capturar_print("erro_preencher.png")
            raise

    def capturar_print(self, nome_arquivo="erro.png"):
        if self.driver:
            caminho = f"logs/{nome_arquivo}"
            self.driver.save_screenshot(caminho)
            logger.info(f"Screenshot salvo: {caminho}")

    def fechar(self):
        if self.driver:
            self.driver.quit()
            logger.info("Navegador fechado com sucesso.")

    def __enter__(self):
        self.iniciar()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fechar()
