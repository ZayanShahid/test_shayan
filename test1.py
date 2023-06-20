from flask import Flask

URL = "https://www.google.com"
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    
    app.run()



