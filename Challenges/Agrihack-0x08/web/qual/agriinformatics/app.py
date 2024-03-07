#!/usr/bin/env python3
import flask
import sqlite3

app = flask.Flask(__name__)

def db_search(code):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM community WHERE code=UPPER('{code}')")
        found = cur.fetchone()
    return None if found is None else found[0]

@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/api/search', methods=['POST'])
def api_search():
    req = flask.request.get_json()
    if 'code' not in req:
        flask.abort(400, "Empty community code")

    code = req['code']
    if len(code) > 4 or "'" in code:
        flask.abort(400, "Invalid community code")

    name = db_search(code)
    if name is None:
        flask.abort(404, "No such community")

    return {'name': name}

if __name__ == '__main__':
    app.run(debug=True)
