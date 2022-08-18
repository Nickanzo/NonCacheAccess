import unittest
from bin.dbCon import *
from settings import *


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here

#Teste Banco de Dados
if __name__ == '__main__':
    # |✓| 1° Teste, criar conexão
    con = create_con(HOST,USER,PASSWORD,NAME)

    # |✓| 2° Teste, verifica conexão com o BD
    if(con.is_connected()):
        print("Conexão com sucesso")
    else:
        print("Falhou")

    # |✓| 3° Teste, cria usuários
    # |✓| 5° Teste, evita duplicidade no banco e no SQL
    create_user(con, 'pepito', 'pepo123')
    create_user(con, 'pepita', 'pepa123')
    create_user(con, 'pepite', 'pepe123')
    create_user(con, 'pepiti', 'pepi123')
    create_user(con, 'pepitu', 'pepu123')

    # |✓| 4° Teste, valida usuário criado no BD
    if(verify_user(con, "pepito", "pepo123")):
        print("Login com sucesso")


    # | | 6° Teste, deleta usuários

