import psycopg2
def create_tables():
    commands = ("CREATE TABLE employees(id SERIAL PRIMARY KEY, fname varchar(10),lname varchar(10))")
    conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="s6k6a6t6e6.-", 
                        database="postgres",
                        options="-c search_path=public"
                       )
    cur = conn.cursor()
    cur.execute(commands)
    cur.close()
    conn.commit()
    conn.close()
create_tables()