import sqlite3


DB = "university.db"
QUERY_NUMBER = 5
QUERY_SCRIPT = f"query/query_{QUERY_NUMBER}.sql"


def select_data(query_script):
    
    with open(query_script, "r") as fd:
        sql_sqript = fd.read()
        
    with sqlite3.connect(DB) as connection:
        
        cursor = connection.cursor()              
        cursor.execute(sql_sqript)
        
        return cursor.fetchall()
        
if __name__ == "__main__":
    
    print(select_data(QUERY_SCRIPT))