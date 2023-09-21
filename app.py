import os
import base64
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from cryptography.fernet import Fernet
from flask_sse import sse

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DATABASE'] = 'data.db'
app.config['DATABASE_INIT'] = False

socketio = SocketIO(app)
sse.init_app(app)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def init_db():
    """Initialize the SQLite database if not already initialized."""
    if not app.config['DATABASE_INIT']:
        with app.app_context():
            from flask_sqlalchemy import SQLAlchemy
            db = SQLAlchemy(app)
            db.create_all()
        app.config['DATABASE_INIT'] = True

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('send-data')
def handle_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode()).decode()
    save_to_database(encrypted_data)
    emit('receive-data', encrypted_data, broadcast=True)

def save_to_database(data):
    init_db()
    from models import Data
    new_data = Data(data=data)
    new_data.save()

if __name__ == '__main__':
    socketio.run(app)
