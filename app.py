import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_recruto():
    name = request.args.get('name')
    message = request.args.get('message')
    if not name or not message:
        return render_template('error.html', error="Пожалуйста, укажите параметры 'name' и 'message' в URL.")
    return render_template('hello.html', name=name, message=message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

