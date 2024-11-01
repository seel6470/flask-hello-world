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
