import psycopg2
import itertools
def fill_table(employees):
    commands = ("INSERT INTO employees(fname, lname) VALUES(%s, %s);")
    conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="s6k6a6t6e6.-", 
                        database="postgres",
                        options="-c search_path=public"
                       )
    cur = conn.cursor()
    cur.executemany(commands, employees)
    cur.close()
    conn.commit()
    conn.close()

#I created a list with 25 names and another with 20 last names to fill the table
first = ['John', 'Kelly', 'Pam', 'Micheal', 'Toby', 'Jim', 'Dwight',
        'Ryan', 'Stanley', 'Andy', 'Roy', 'Arthur', 'Bob', 'David',
        'Phillys', 'Meredith', 'Karen', 'Oscar', 'Jan', 'Darryl',
        'John', 'Dan', 'Joe', 'Robert', 'Jo']
last = ['Doe', 'Williams', 'Stark', 'Barnes', 'Rgoers',
        'Danvers', 'Johnson', 'Smith', 'Woods', 'Adams',
        'Wilson', 'Brown', 'Garcia', 'Miller', 'Davis',
        'Thomas', 'Moore', 'Jackson', 'Lee', 'White']

employees = list(itertools.product(first, last))

fill_table(employees)