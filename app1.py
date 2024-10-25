from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route('/app1/<model>')
def indexd(model):
    data = {
        'message': f'hi app1, {model}'
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
