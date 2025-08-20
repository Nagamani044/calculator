from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def api_add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(result=add(a, b))

@app.route('/subtract', methods=['GET'])
def api_subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(result=subtract(a, b))

@app.route('/multiply', methods=['GET'])
def api_multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(result=multiply(a, b))

@app.route('/divide', methods=['GET'])
def api_divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    try:
        result = divide(a, b)
        return jsonify(result=result)
    except ZeroDivisionError as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
