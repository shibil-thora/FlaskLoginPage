from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__) 


@app.route('/')
def index(): 
    return render_template('home.html')  


@app.route('/login_user', methods=['GET', 'POST'])
def login_user(): 
    if request.method == 'GET':
        usr = request.args.get('usr')
        pwd = request.args.get('pwd')
        print('get request', usr, pwd)
    
    if request.method == 'POST': 
        print('post request')

    # login logic 
    response_data = {
        'status': 'nice'
    }
    return jsonify(response_data)

if __name__ == '__main__': 
    app.run()