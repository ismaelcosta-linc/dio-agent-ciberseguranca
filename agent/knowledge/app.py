"""
Laboratório educacional de SQL Injection.
Código intencionalmente vulnerável para análise de segurança.
"""

import sqlite3


def autenticar(usuario, senha):
    conexao = sqlite3.connect(":memory:")

    conexao.execute(
        "CREATE TABLE usuarios (usuario TEXT, senha TEXT)"
    )

    conexao.execute(
        "INSERT INTO usuarios VALUES ('admin', 'senha_teste')"
    )

    consulta = (
        "SELECT * FROM usuarios WHERE usuario = '"
        + usuario
        + "' AND senha = '"
        + senha
        + "'"
    )

    resultado = conexao.execute(consulta).fetchone()
    conexao.close()

    return resultado is not None


if __name__ == "__main__":
    print("Laboratório de autenticação SQLite")
    print("Código intencionalmente vulnerável.")
