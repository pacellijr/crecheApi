"""
Modulo TURMA. Suporta as ações ReST para a coleção de turmas
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
TURMAS = {
    "B1": {
        "sigla": "B1",
        "nome": "Bercario 1",
        "timestamp": get_timestamp(),
    },
    "B2": {
        "sigla": "B2",
        "nome": "Bercario 2",
        "timestamp": get_timestamp(),
    },
    "MTZ": {
        "sigla": "MTZ",
        "nome": "Maternalzinho",
        "timestamp": get_timestamp(),
    },
    "M1": {
        "sigla": "M1",
        "nome": "Maternal 1",
        "timestamp": get_timestamp(),
    },
    "M2": {
        "sigla": "M2",
        "nome": "Maternal 2",
        "timestamp": get_timestamp(),
    },
    "P1": {
        "sigla": "P1",
        "nome": "Pre 1",
        "timestamp": get_timestamp(),
    },
    "P2": {
        "sigla": "P2",
        "nome": "Pre 2",
        "timestamp": get_timestamp(),
    },
    
}


def read_all(length, offset):
    """
    Essa função responde a requisições a /api/turma
    e retorna a lista completa de turmas
    :return:        json string of list of turma
    """
    # Create the list of people from our data
    return [TURMAS[key] for key in sorted(TURMAS.keys())[offset:(length+offset)]]


def read_one(sigla):
    """
    Essa função responde a requisições a /api/turma/{sigla}
    com uma turma encontrada na lista de turmas
    :param sigla:   sigla da turma a encontrar
    :return:        turma com o nome apresentado
    """
    # Does the person exist in people?
    if sigla in TURMAS:
        turma = TURMAS.get(sigla)

    # otherwise, nope, not found
    else:
        abort(
            404, "Turma com a sigla {sigla} não encontrada".format(sigla=sigla)
        )

    return turma


def create(turma):
    """
    Essa função cria uma nova turma na estrutura de turmas
    baseado nos dados passados
    :param turma:   turma a ser criada na estrutura de turmas
    :return:        201 se sucesso, 406 se turma já existe
    """

    sigla = turma.get("sigla", None)
    nome  = turma.get("nome", None)
    
    # A turma já existe?
    if sigla not in TURMAS and sigla is not None:
        TURMAS[sigla] = {
            "sigla": sigla,
            "nome": nome,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{sigla} criada com sucesso".format(sigla=sigla), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Turma com sigla {sigla} já existe".format(sigla=sigla),
        )


def update(sigla, turma):
    """
    Essa função atualiza uma turma já existente na estrutura de turmas
    :param sigla:   sigla da turma para atualizar na estrutura de turmas
    :param turma:   turma para atualizar
    :return:        turma (da estrutura) atualizada
    """
    # A turma existe na lista de turmas?
    if sigla in TURMAS:
        TURMAS[sigla]["nome"] = turma.get("nome")
        TURMAS[sigla]["timestamp"] = get_timestamp()

        return TURMAS[sigla]

    # caso contrário, não, há um erro
    else:
        abort(
            404, "Turma com sigla {sigla} não encontrada".format(sigla=sigla)
        )


def delete(sigla):
    """
    Essa função remove uma turma da estrutura de turmas
    :param sigla:   sigla da turma a remover
    :return:        200 caso remoção bem sucedida, 404 se não encontrada
    """
    # Does the person to delete exist?
    if sigla in TURMAS:
        del TURMAS[sigla]
        return make_response(
            "{sigla} removida com sucesso".format(sigla=sigla), 200
        )

    # Caso contrário, não, a turma a remover não foi encontrada
    else:
        abort(
            404, "Turma com sigla {sigla} não encontrada".format(sigla=sigla)
        )
