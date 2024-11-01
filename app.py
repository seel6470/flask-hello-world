from flask import Flask
import psycopg2
import prefix
app = Flask(__name__)
prefix.use_PrefixMiddleware(app)

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


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)
