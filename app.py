from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World from Seth Ely (seel6470) in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_test_db_user:tQ7u6YUYctCEThZ8765T9Bq38FDzJiI8@dpg-csifge1u0jms73fbcag0-a/lab_10_test_db")
    conn.close()
    return "Test DB connection successful!"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("your_db_url_here")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("your_db_url_here")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("your_db_url_here")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    conn.close()

    response = "<table><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    for row in records:
        response += "<tr>"
        for item in row:
            response += f"<td>{item}</td>"
        response += "</tr>"
    response += "</table>"
    return response

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("your_db_url_here")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Basketball;")
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"
