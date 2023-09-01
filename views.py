from utils import load_template, load_data
import json


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith("POST"):
        request = request.replace("\r", "")  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split("\n\n")
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split("&"):
            chave, valor = chave_valor.split("=")
            params[chave] = valor
        print(params)
        with open("data/dados.json", "w") as file:
            json.dump(params, file)
        return "HTTP/1.1 200 OK\r\n\r\n" + load_template("index.html").format(
            titulo=params["titulo"], descricao=params["descricao"]
        )
    note_template = load_template("components/note.html")
    notes_li = [
        note_template.format(title=dados["titulo"], details=dados["detalhes"])
        for dados in load_data("notes.json")
    ]
    notes = "\n".join(notes_li)

    return load_template("index.html").format(notes=notes).encode()
