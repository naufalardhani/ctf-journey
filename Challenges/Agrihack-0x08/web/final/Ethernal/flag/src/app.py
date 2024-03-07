from flask import Flask, request, render_template, redirect, url_for, render_template_string, jsonify

app = Flask(__name__)

@app.route('/flag', methods=['POST'])
def index():
    if request.form.get('flag') == 'show':
        return "agrihack{d6723612-b6fa-4f7f-8198-c488765dcbcd}"
    else:
        return "Invalid request"

if __name__ == '__main__':
    app.run()