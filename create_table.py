from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        

if __name__ == "__main__":
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMERY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text
    );
    """
    
    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        name text NOT NULL,
        priority integet,
        projects_id integer NOT NULL,
        status Boolean default False,
        begin_date text NOT NULL,
        ens_date text NOT NULL,
        FOREIGN KEY (projects_id) REFERENCES projects (id)
    );
    """
    
    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_projects_table)
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! Cannot create the database connection.")