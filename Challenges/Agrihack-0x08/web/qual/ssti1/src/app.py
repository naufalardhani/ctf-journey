from flask import Flask, request, render_template, redirect, url_for, render_template_string, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', chall="ssti1")

@app.route('/welcome', methods=['GET'])
def welcome():
    urname = request.args.get('name')
    return render_template_string(f'Welcome {urname}')

if __name__ == '__main__':
    app.run()