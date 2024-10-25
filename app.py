from flask import Flask, jsonify, redirect

app = Flask(__name__) 
server_url = '3.110.212.33'

@app.route('/')
def index():
    data = {
        'message': 'hi app'
    }
    return jsonify(data)

@app.route('/app1')
def index1():
    return redirect(f"http://{server_url}:8001/app1")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
