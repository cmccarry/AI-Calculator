# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from utility import evaluate_expression

# Initialize Flask app
app = Flask(__name__)

# Global variable to store the equation input
equation = ""

# Route for the home page
@app.route("/")
def index():
    return render_template('index.html')

# Endpoint for updating the equation
@app.route('/update_equation', methods=['POST'])
def update_equation():
    global equation
    equation = request.json.get('equation', "")
    return jsonify({'message': 'Equation updated successfully'})

# Endpoint for evaluating the equation
@app.route('/evaluate', methods=['POST'])
def evaluate():
    global equation
    # Call the function to evaluate the equation using the AI model
    result = evaluate_expression(equation)
    
    # Return the result and ask if they want additional work
    return jsonify({'result': result, 'additional_work_prompt': 'Would you like to see step-by-step work?'})

# Endpoint for additional work
@app.route('/additional_work', methods=['POST'])
def additional_work():
    global equation
    # Call the function to show additional work using the AI model
    additional_work = evaluate_expression(equation, show_work=True)
    
    # Return the step-by-step work
    return jsonify({'additional_work': additional_work})

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
