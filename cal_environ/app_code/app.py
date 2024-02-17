from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
#Define routes for arithmetic operations

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})


@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 - num2
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 / num2
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return jsonify({'result': result})



if __name__ == '__main__':
    app.run(debug=True)