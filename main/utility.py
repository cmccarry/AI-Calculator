"""
At the command line, install the package via pip if not done already:

$ pip install google-generativeai
"""

# Import the necessary libraries
import google.generativeai as genai
from credentials import google_api_key

# Configure the Google Generative AI library with the API key
genai.configure(api_key=google_api_key)

# Set up the model generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

# Define safety settings for content generation
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

def evaluate_expression(expression, show_work=False):
    # Initialize the generative model
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config, safety_settings=safety_settings)

    # Start a conversation with the model
    convo = model.start_chat(history=[])

    # Construct the message to evaluate the expression
    message = f"Here is a mathematical expression: {expression}. Can you evaluate it?"
    
    if show_work:
        message += " Please show the step-by-step work as well."

    # Send the message to the model
    convo.send_message([message])

    # Check the AI's response
    if convo.last.text:
        return convo.last.text
    else:
        return "There was an issue processing the equation. Please try again."

