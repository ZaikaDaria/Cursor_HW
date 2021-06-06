from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/calc/<int:a>/<int:b>/div')
def div(a, b):
    try:
        return render_template("div.html", a=a, b=b, result=a / b)
    except ZeroDivisionError:
        return "You cannot divide by zero!"


@app.route('/calc/<int:a>/<int:b>/sum')
def sum(a, b):
    return render_template("sum.html", a=a, b=b, result=a + b)


@app.route('/calc/<int:a>/<int:b>/sub')
def sub(a, b):
    return render_template("sub.html", a=a, b=b, result=a - b)


@app.route('/calc/<int:a>/<int:b>/mult')
def mult(a, b):


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")