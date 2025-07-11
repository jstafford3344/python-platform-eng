from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def get_info():
    return jsonify({
        "time": datetime.datetime.now(),
        "hostname": socket.gethostname(),
        "msg": "Triggering Github Actions run",
        "deployed_on": "kubernetes"
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")