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

    sql1 = """
        SELECT COUNT(*), c.company_name
        FROM employees e
        LEFT JOIN companies c ON e.company_id = c.id
        GROUP BY c.id
    """
    sql2 = """
        SELECT c.company_name, e.employee, p.total
        FROM companies c
        LEFT JOIN employees e ON e.company_id = c.id
        LEFT JOIN payments p ON p.employee_id = e.id
        WHERE p.total > 5000 AND p.date_of LIKE '2023-07-%'
    """
    
    print(execute_sql_script(sql2))
