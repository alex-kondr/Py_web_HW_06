import sqlite3
import os


BASE_DIR = os.path.dirname(__file__)
DB = os.path.join(BASE_DIR, "salary.db")

print(DB)


def execute_sql_script(sql: str) -> list:

    with sqlite3.connect(DB) as db:

        cursor = db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == "__main__":

    sql = """
        SELECT COUNT(*), c.company_name
        FROM employees e
        LEFT JOIN companies c ON e.company_id = c.id
        GROUP BY c.id
    """    
    print(execute_sql_script(sql))
