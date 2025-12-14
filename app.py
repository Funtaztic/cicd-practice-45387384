import os
import psycopg2
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Get DB info from the Docker Compose environment variables
DB_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DB_URL)
    return conn

def init_db():
    """Create the table if it doesn't exist."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS messages (content TEXT);')
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")

# Run this once on startup
if DB_URL:
    init_db()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Save data from the box
        content = request.form['content']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO messages (content) VALUES (%s)', (content,))
        conn.commit()
        cur.close()
        conn.close()

    # Get all data to display
    messages = []
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT content FROM messages;')
        messages = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
    except:
        pass

    return """
    <html>
        <body>
            <h1>Multi-Container App! 📦 + 📦</h1>
            <form method="POST">
                <input type="text" name="content" placeholder="Type something...">
                <input type="submit" value="Save to DB">
            </form>
            <hr>
            <h3>Saved Messages:</h3>
            <ul>
                """ + "".join([f"<li>{msg}</li>" for msg in messages]) + """
            </ul>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
