import random
import string
import json
from flask import Flask, request, render_template, redirect, url_for, render_template_string, jsonify

app = Flask(__name__)
app.config['FLAG_LOCATION'] = '/flag-12893u9n1e981.txt'
app.config['FLAG_READER'] = '/readflag?name=flag.txt'

request_data = {}
path_mapping = {}  
owner_agents = {} 


def filter(string):
    blacklists = ['config', 'class', 'mro', 'import', 'builtins', 'popen', 'system', 'eval', 'exec', 'url_for', 'request', 'update', 'subprocess', '\..', ',', "''", '[]', '_', '*', '+', '-', '~', '>', '<',]
    for word in blacklists:
        if word in string:
            return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        path = request.form.get('path')
        user_agent = request.headers.get('User-Agent')
        if path:
            if path in request_data:
                if owner_agents.get(path) == user_agent:
                    if filter(path):
                        return render_template_string(f"Path {path} already exists. Please enter a new path.")
                    else:
                        return "mang lu kira gweh beneran ssti?"
                else:
                    random_hex = generate_random_hex()
                    path_mapping[random_hex] = path
                    owner_agents[path] = user_agent
                    request_data[path] = []
                    # save_to_json() 
                    return redirect(url_for('catch_requests', path=random_hex))
            else:
                random_hex = generate_random_hex()
                path_mapping[random_hex] = path
                owner_agents[path] = user_agent
                request_data[path] = []
                # save_to_json()
                return redirect(url_for('catch_requests', path=random_hex))
    
    paths = list(request_data.keys())
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', paths=paths, ua=user_agent)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def catch_requests(path):
    user_provided_path = path_mapping.get(path)
    user_agent = request.headers.get('User-Agent')
    
    if user_provided_path:
        owner_agent = owner_agents.get(user_provided_path)
        
        if owner_agent == user_agent:
            if request.method in ['POST', 'PUT', 'PATCH']:
                req_data = request.get_data(as_text=True)
            else:
                req_data = None

            request_data[user_provided_path].append({
                'method': request.method,
                'path': request.full_path,
                'headers': dict(request.headers),
                'data': req_data
            })
            # save_to_json()  

            return render_template('path_detail.html', path=user_provided_path, request_data=request_data[user_provided_path], ua=user_agent, hex=path)
        else:
            return "Unauthorized access."
    else:
        blacklist = ['url_for']
        for x in blacklist:
            if x in path:
                return "mang lu kira gweh beneran ssti?"
        return f"{path} not found"
    
@app.route('/readflag', methods=['GET'])
def baca_file_get():
    try:
        filename = request.args.get('name')

        if filename == app.config['FLAG_LOCATION']:
            with open(filename, 'r') as file:
                file_content = file.read()
            return jsonify({'status': 'success', 'message': 'File read successfully', 'file_content': file_content})
        else:
            return jsonify({'status': 'error', 'message': 'File name not provided'})

    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)})

def generate_random_hex(length=30):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == '__main__':
    app.run()
