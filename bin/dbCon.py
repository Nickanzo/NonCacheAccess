import mysql.connector


def create_con(host, user, password, db):
    return mysql.connector.connect(host=host, user=user, password=password, database=db)


def close_con(con):
    return con.close()


def create_user(con, user, password):
    if (con.is_connected()):
        if(bool(verify_user(con, user, password)) == False):
            cursor = con.cursor()
            sql = "INSERT INTO login (username, password) values (%s, %s)"
            values = (user, password)
            cursor.execute(sql, values)
            cursor.close()
            con.commit()
        else:
            print("Usuário já existe")
    else:
        print("DB conection error")


def verify_user(con, user, password):
    if(con.is_connected):
        cursor = con.cursor()
        sql = "SELECT COUNT(*) FROM login WHERE username = %s AND password = %s"
        values = (user, password)
        cursor.execute(sql, values)
        (rows,) = cursor.fetchone()
        cursor.close()

        return bool(rows)
