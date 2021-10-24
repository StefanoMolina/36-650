import psycopg2
def print_query():
    command = (" SELECT * FROM employees where id <= 10")
    conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="s6k6a6t6e6.-", 
                        database="postgres",
                        #You may add the following line if you have schemaa
                        options="-c search_path=public"
                       )
    cur = conn.cursor()
    cur.execute(command)
    for table in cur.fetchall():
        print(table)
    cur.close()
    conn.commit()
    conn.close()