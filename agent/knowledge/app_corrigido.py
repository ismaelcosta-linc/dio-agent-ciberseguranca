"""Laboratório de autenticação com parâmetros SQL e hash de senha.

O cadastro existe apenas durante a execução, em um banco em memória.
"""

import hashlib
import hmac
import secrets
import sqlite3
from contextlib import closing
from getpass import getpass


ITERACOES_PBKDF2 = 600_000


def derivar_hash(senha, salt, iteracoes):
    """Deriva um hash lento; o salt aleatório diferencia senhas iguais."""
    return hashlib.pbkdf2_hmac(
        "sha256", senha.encode("utf-8"), salt, iteracoes
    )


def cadastrar_usuario(conexao, usuario, senha):
    if not usuario.strip() or not senha:
        raise ValueError("Informe um usuário e uma senha não vazios.")

    salt = secrets.token_bytes(16)
    senha_hash = derivar_hash(senha, salt, ITERACOES_PBKDF2)
    # Este contexto confirma a transação ou a desfaz em caso de erro.
    with conexao:
        conexao.execute(
            "INSERT INTO usuarios (usuario, salt, senha_hash, iteracoes) "
            "VALUES (?, ?, ?, ?)",
            (usuario, salt, senha_hash, ITERACOES_PBKDF2),
        )


def autenticar(conexao, usuario, senha):
    registro = conexao.execute(
        "SELECT salt, senha_hash, iteracoes FROM usuarios WHERE usuario = ?",
        (usuario,),
    ).fetchone()

    # Faz a derivação também para usuários inexistentes, evitando uma saída
    # imediata que facilitaria distinguir contas pelo tempo de resposta.
    if registro is None:
        salt = secrets.token_bytes(16)
        hash_esperado = bytes(32)
        iteracoes = ITERACOES_PBKDF2
    else:
        salt, hash_esperado, iteracoes = registro

    hash_informado = derivar_hash(senha, salt, iteracoes)
    confere = hmac.compare_digest(hash_informado, hash_esperado)
    return registro is not None and confere


def main():
    print("Laboratório de autenticação SQLite corrigido")
    print("Use dados fictícios. O cadastro será descartado ao encerrar.")
    usuario = input("Crie um usuário: ")
    senha = getpass("Crie uma senha de teste: ")

    # closing garante close() mesmo se ocorrer uma exceção.
    # O contexto de uma conexão SQLite, sozinho, não fecha a conexão.
    with closing(sqlite3.connect(":memory:")) as conexao:
        conexao.execute(
            "CREATE TABLE usuarios ("
            "usuario TEXT PRIMARY KEY, "
            "salt BLOB NOT NULL, "
            "senha_hash BLOB NOT NULL, "
            "iteracoes INTEGER NOT NULL)"
        )
        cadastrar_usuario(conexao, usuario, senha)
        del senha

        usuario_login = input("Usuário para autenticar: ")
        senha_login = getpass("Senha: ")
        autenticado = autenticar(conexao, usuario_login, senha_login)
        del senha_login
        print("Autenticado." if autenticado else "Credenciais inválidas.")


if __name__ == "__main__":
    main()
