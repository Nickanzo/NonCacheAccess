import mysql.connector


def create_con(host, user, password, db):
    return mysql.connector.connect(host=host, user=user, password=password, database=db)


def close_con(con):
    return con.close()
