import subprocess

from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method != 'POST':
        abort(501)

    data = request.get_json()

    if data['ref'].endswith('/master'):
        subprocess.call(['./build_site.sh'])

    return '', 204

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 9001
    app.run(host=host, port=port)
