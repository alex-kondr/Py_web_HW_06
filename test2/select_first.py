import sqlite3
import os.path


DB = os.path.join(os.path.dirname(__file__), "salary.db")

# print(DB)


def execute_query(sql: str) -> list:
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(payments.total), 2), employees.post
FROM payments
LEFT JOIN employees ON payments.employee_id = employees.id
GROUP BY employees.post
"""

print(execute_query(sql))
