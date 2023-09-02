from utils import load_data, load_template, build_response
from database import Database
from database import Note
from urllib.parse import unquote_plus

database = Database("notes")


def delete(request):
    request = request.replace("\r", "")
    body = request.split("\n\n")[1]
    note_id = body.split("=")[1]

    database.delete(note_id)
    response = build_response(code=303, headers="Location: /")

    return response


def edit(request):
    request = request.replace("\r", "")  # Remove caracteres indesejados
    partes = request.split("\n\n")
    corpo = partes[1]
    print(corpo)
    note_id = corpo.split("=")[1]
    note = database.get(note_id)
    response = build_response(
        body=load_template("edit.html").format(
            id=note.id, title=note.title, content=note.content
        )
    )
    return response


def update(request):
    request = request.replace("\r", "")  # Remove caracteres indesejados
    partes = request.split("\n\n")
    corpo = partes[1]
    note_id = corpo.split("&")[0].split("=")[1]
    title = unquote_plus(corpo.split("&")[1].split("=")[1])
    content = unquote_plus(corpo.split("&")[2].split("=")[1])
    database.update(Note(id=note_id, title=title, content=content))

    response = build_response(code=303, reason="See Other", headers="Location: /")
    return response


def not_found(request):
    response = build_response(code=404, body=load_template("not_found.html"))
    return response


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith("POST"):
        request = request.replace("\r", "")  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split("\n\n")
        corpo = partes[1]
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        itens = [0, 0]
        for chave_valor in corpo.split("&"):
            chave, valor = chave_valor.split("=")
            if chave == "titulo":
                itens[0] = unquote_plus(valor)
            elif chave == "detalhes":
                itens[1] = unquote_plus(valor)

        database.add(Note(title=itens[0], content=itens[1]))
        response = build_response(code=303, reason="See Other", headers="Location: /")
        return response

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    """note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))"""

    notes = database.get_all()
    note_template = load_template("components/note.html")
    notes_li = [
        note_template.format(title=note.title, details=note.content, id=note.id)
        for note in notes
    ]
    notes = "\n".join(notes_li)
    response = build_response(body=load_template("index.html").format(notes=notes))
    return response
