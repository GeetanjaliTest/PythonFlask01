from flask import Flask
app = Flask(__name__)

myname = "test"
@app.route('/')
def hello_world():
    return 'Hello World!' + myname


if __name__ == '__main__':
    app.run(port=5001, debug=True)