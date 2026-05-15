import psycopg2 as pg
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = pg.connect(
        host="localhost", port=5432, dbname="postgres", user="postgres", password=3333,
    )
    cur = conn.cursor()
    cur.execute("select * from actor")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('app.html', rows=rows)