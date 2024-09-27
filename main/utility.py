import google.generativeai as genai
from credentials import google_api_key

# Configure the API key
genai.configure(api_key=google_api_key)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

# Define safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

def evaluate_expression(expression):
    # Start a conversation with the model
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    convo = model.start_chat(history=[])

    # Send the message to the model
    convo.send_message([
        "Evaluate the following mathematical expression."
        "Do not use any boldening or punctuation just say the expression and = the answer."
        "If the expression is more than one step, go through the steps in the result as well."
        ,expression
    ])

    # Get and return the response from the model
    if convo.last.text:
        return convo.last.text
    else:
        return "Could not evaluate the expression."
