from flask import Flask, render_template, request, jsonify
from utility import evaluate_expression

app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for evaluating the expression
@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    expression = data.get('expression', '')

    # Call the evaluate the expression
    result = evaluate_expression(expression)
    
    return jsonify({'result': result})

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
