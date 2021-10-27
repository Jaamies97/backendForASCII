from flask import Flask

app = Flask(__name__)

@app.route('/axel_ojut/<username>')
def hello_world(username):
    return f'<h1>Hello Axel and {username}!</h1>'

if __name__ == '__main__':
    app.run()