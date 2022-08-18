import unittest
from bin.dbCon import create_con, close_con
from settings import *


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    con = create_con(HOST,USER,PASSWORD,NAME)

    if(con.is_connected()):
        print("Conexão com sucesso")
    else:
        print("Falhou")

