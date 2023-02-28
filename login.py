from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return f'Hello World From Login!!!!'
    if request.method == 'POST':
        username = request.form['username']
        if username == 'akash':
         return f'sucessfully login as {username}'
        else: 
         return f'invalid login'
        #username = request.form['username']
        #print(username)
        #return f'Logged in as {username}' 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        #return f'Hello World !!!!'
        return redirect(url_for('login'))
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        return url_for('login')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
