from pathlib import Path
import json


def extract_route(request):
    return request.split()[1].lstrip("/")


def read_file(path: Path):
    # recebe um argumento do tipo Path e devolve
    # o conteúdo desse arquivo. Sua função deve
    # ler o arquivo e devolver o conteúdo como
    # binário (bytes).
    with open(path, "rb") as file:
        return file.read()
    pass


def load_data(filename: str):
    """
    que recebe o nome de um arquivo JSON e devolve
    o conteúdo do arquivo carregado como um objeto
    Python (A função deve assumir que este arquivo
    JSON está localizado dentro da pasta data).
    Por exemplo: se o conteúdo do arquivo data/dados.json
    for a string {"chave": "valor"}, sua função deve devolver
    o dicionário Python {"chave": "valor"} para a entrada dados.json
    """
    with open("data/" + filename, "r") as file:
        return json.load(file)
    pass


"""
Implemente a função load_template que recebe o nome de um arquivo de template e devolve uma string com o conteúdo desse arquivo.
 O nome do arquivo não inclui o nome da pasta templates.
Por exemplo: para a entrada index.html você deve carregar o conteúdo do arquivo templates/index.html.
"""


def load_template(filename: str):
    with open("templates/" + filename, "r") as file:
        return file.read()
    pass


def build_response(body="", code=200, reason="OK", headers=""):
    "Retorna a resposta do servidor"
    if headers == "":
        headers = "Content-Type: text/html; charset=utf-8"
    return (f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}").encode("utf-8")
