from flask import Flask, request, render_template, redirect, url_for, render_template_string, jsonify

app = Flask(__name__)
app.config['FLAG'] = 'agrihack{1ntr0duct10n_to_e4sy_j1nj42_ssti}'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['GET'])
def welcome():
    urname = request.args.get('name')
    return render_template_string(f'Welcome {urname}')

if __name__ == '__main__':
    app.run()