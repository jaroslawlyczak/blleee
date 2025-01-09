from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
<!DOCTYPE html>
<html>
<head>
    <title>Enter Your Name</title>
</head>
<body>
    <form method="POST" action="/">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        return f'<h1>Hello, {name}!</h1>'
    return html_form

@app.route('/hello/<name>')
def hello_name(name):
    return f'<p>Hello, {name}!</p>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)