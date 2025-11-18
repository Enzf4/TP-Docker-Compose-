from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return jsonify({
        'message': 'Olá do Container Flask!',
        'hostname': hostname,
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'online',
        'porta': '8081'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/info')
def info():
    return jsonify({
        'servico': 'Aplicação Flask Simples',
        'versao': '1.0',
        'container': 'flask-app'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
