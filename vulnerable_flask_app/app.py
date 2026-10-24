import os
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
# Secret lu depuis l'environnement, plus de valeur codee en dur
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24).hex())

@app.route('/')
def index():
    return """
    <h1>Welcome to our fixed Flask App!</h1>
    <ul>
        <li><a href="/hello?name=World">Hello Page</a></li>
    </ul>
    """

@app.route('/hello')
def hello():
    name = escape(request.args.get('name', 'Guest'))
    return f"""
    <h1>Hello Page</h1>
    <p>Hello, {name}!</p>
    <p><a href="/">Back to Homepage</a></p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
