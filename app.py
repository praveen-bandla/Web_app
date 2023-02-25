from flask import Flask, g, render_template, request, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = 'data/messages.db'
NUM_MESSAGES = 5

@app.route("/")
def main():
    return render_template('main.html')


@app.route("/submit/", methods = ['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template("submit.html")
    else:
        insert_message(request)
        return render_template("submit.html",
                               name = request.form['name'],
                               message = request.form['message'])


@app.route("/view/")
def view():
    messages = random_messages(NUM_MESSAGES)
    return render_template("view.html", messages = messages)


def get_message_db():
    '''
    Get's connection to database with messages if exists. If not, creates
    '''
    try:
        #returns database if exists
        return g.message_db

    except:
        #creating a database
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            #command for sql
            cmd = """
            CREATE TABLE IF NOT EXISTS messages (
            id INTEGER IDENTITY PRIMARY KEY,
            name TEXT,
            message TEXT);
            """
            cur.execute(cmd)
            conn.commit()
            g.message_db = conn
            return g.message_db



def insert_message(request):
    '''
    Inserts message into database
    '''
    conn = get_message_db()
    cur = conn.cursor()

    #Getting form data
    name = request.form['name']
    message = request.form['message']

    #Inserting data into database
    cur.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    conn.commit()

    #closing the sql connection
    conn.close()



def random_messages(n):
    '''
    Returns random messages
    '''
    conn = get_message_db()
    cur = conn.cursor()

    #command for sql
    cmd = """
    SELECT * FROM messages
    ORDER BY RANDOM()
    LIMIT (?)
    """
    cur.execute(cmd, (n,))
    rows = cur.fetchall()

    #generating messages from the database
    messages = [(r[1], r[2]) for r in rows]

    #closing the sql connection
    conn.close()

    return messages