from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('./index1.html')

@socketio.on('keypress')
def handle_keypress(data):
    key = data['key']
    emit('keypress', key, broadcast=True)

if __name__ == '__main__':
    socketio.run(app,debug=True)
# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def hello_world():
#     return "hello world2"
# if __name__=="__main__":
#     app.run(debug=True,port=8000)
