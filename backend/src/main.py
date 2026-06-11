import os
import psycopg2
import logging
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder ='/app/frontend/templates/', static_folder = '/app/frontend/static/')

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

@app.route('/')
def index():
    app.logger.debug('Fetching all tasks from the database')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todo;')
    todos = cur.fetchall()
    app.logger.debug(todos)
    cur.close()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    due_date = request.form['due_date']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO todo (task, due_date) VALUES (%s, %s)', (task, due_date))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    app.logger.debug(f'Deleting task with id: {id}')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM todo WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 


