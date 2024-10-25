from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route('/app1')
def index():
    data = {
        'message': 'hi app1'
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
