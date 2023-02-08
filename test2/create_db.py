import sqlite3


data_base = "salary.db"
sql_script_salary = "salary.sql"

def create_db():
    
    with open(sql_script_salary, "r") as fd:
        sql_script = fd.read()
        
    with sqlite3.connect(data_base) as connection:
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        

if __name__ == "__main__":
    create_db()