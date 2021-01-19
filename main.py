from flask_socketio import SocketIO
from flask import Flask, request, render_template, Response, send_from_directory, jsonify
import subprocess

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')

def play_mp3(url, topic):
    try:
        socketio.emit('change', topic)
        curl = subprocess.Popen(['curl', '--silent', url], stdout=subprocess.PIPE)
        mpg = subprocess.Popen(['mpg123', '-q', '-a', 'hw:1,0', '-'], stdin=curl.stdout, stdout=subprocess.PIPE).wait()
    except:
        print("nix fehler gut")
    finally:
        socketio.emit('change', 'waiting')

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/small')
def small():
    return render_template('small.html')

@app.route('/large')
def large():
    return render_template('large.html')

@app.route('/change', methods=['POST'])
def change():
    topic = request.json['topic']
    if topic == "news":
        thread = socketio.start_background_task(play_mp3, request.json['url'], topic)
    return jsonify({"state": "ok"})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
