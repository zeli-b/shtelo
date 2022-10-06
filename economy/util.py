from typing import Optional

from pymysql import connect
from pymysql.connections import Connection
from pymysql.cursors import DictCursor

database: Optional[Connection] = None


def init(host: str, user: str, password: str, db: str):
    global database

    database = connect(host=host, user=user, password=password, db=db)


def get_value(code: str) -> float:
    assert database is not None

    with database.cursor(DictCursor) as cursor:
        cursor.execute('SELECT value FROM total_value WHERE code = %s', code)
        result = cursor.fetchall()[0]
    return result['value']
