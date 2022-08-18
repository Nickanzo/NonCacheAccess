from dbCon import *
from settings import *

def login(username, password):
    con = create_con(HOST, USER, PASSWORD, NAME)

    if(con.is_connected()):
        if(verify_user(con, username, password)):
            print("Login com sucesso")
        else:
            print("Erro Usuário ou Senha")
    else:
        print("Erro na conexão com o Banco")

