import sqlite3


def create_db(db: str, sql_script: str) -> None:
    
    with open(sql_script, "r") as fd:
        script = fd.read()
        
    with sqlite3.connect(db) as connection:
        cursor = connection.cursor()
        cursor.executescript(script)
    
    
if __name__ == "__main__":
    
    db = "university.db"
    create_table_script = "create_table_script.sql"
    
    create_db(db, create_table_script)
    
