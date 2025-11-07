import re
import time

def formatar_telefone(telefone_bruto: str, ddd_padrao: str = "38") -> str | None:
    
    if telefone_bruto is None:
        return None

    s = str(telefone_bruto).split('/')[0]
    s = re.sub(r"[^\d]", "", s)

    match = re.search(r"\d{8,11}", s)
    if not match:
        return None

    num = match.group(0)
    if len(num) in (8, 9):
        return ddd_padrao + num
    # já tem DDD
    return num

def timestamp_br() -> str:
    return time.strftime("%d/%m/%Y %H:%M:%S")

def apenas_digitos(texto: str) -> str:
    if texto is None:
        return ""
    return re.sub(r"\D", "", str(texto))

def clean_text(texto: str) -> str:
    if not texto:
        return ""
    texto_limpo = (
        str(texto)
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("\t", " ")
        .strip()
    )
    # Remove múltiplos espaços seguidos
    texto_limpo = " ".join(texto_limpo.split())
    return texto_limpo

