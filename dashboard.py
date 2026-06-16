import sqlite3
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("attacks.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM attacks")
    total = cur.fetchone()[0]

    cur.execute('''
    SELECT ip, username, password,
           timestamp, technique,
           country, city
    FROM attacks
    ORDER BY id DESC
    ''')

    attacks = cur.fetchall()

    cur.execute('''
    SELECT password, COUNT(*)
    FROM attacks
    GROUP BY password
    ORDER BY COUNT(*) DESC
    LIMIT 5
    ''')

    chart = cur.fetchall()
    conn.close()

    labels = [x[0] for x in chart]
    values = [x[1] for x in chart]

    return render_template(
        "index.html",
        attacks=attacks,
        total=total,
        labels=json.dumps(labels),
        values=json.dumps(values)
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
