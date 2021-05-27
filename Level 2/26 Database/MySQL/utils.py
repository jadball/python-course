import mysql.connector


def getConnection():
    return mysql.connector.connect(
        host="localhost",
        user="user1",
        password="user1"
    )


def getCursor(connection, table):
    cursor = connection.cursor(buffered=True)
    SQL = f"SELECT * FROM {table}"
    cursor.execute(SQL)
    return cursor
