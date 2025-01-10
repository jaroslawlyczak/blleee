from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Hello, World!</h3><br><br><p>Enter your name in address after slash, ex. 127.0.0.1:5000/Name</p>"

@app.route("/<name>")
def greet(name):
    return f"<h2>Witaj, {name.capitalize()}!</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)