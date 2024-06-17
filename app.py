from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_recruto():
    name = request.args.get('name')
    message = request.args.get('message')
    if not name or not message:
        return "<html><body><h1>Пожалуйста, укажите параметры 'name' и 'message' в URL.</h1></body></html>"
    return render_template('hello.html', name=name, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
