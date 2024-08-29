import signal
import sys
import socket
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS support

# Replace with your API key and base URL if needed
api_key = 'sk-CRIeTtB7ily8Tyrq577d9a2dC628484bB1C8C0B566A69200'
base_url = 'https://oneapi.xty.app/v1'

openai.api_key = api_key
openai.api_base = base_url

@app.route('/generate', methods=['POST'])
def generate():
    # Print request data for debugging
    print("Received request data:", request.json)
    
    data = request.json
    model = data.get('model')
    # Extract prompt from the 'messages' field
    prompt = data['messages'][0]['content'] if 'messages' in data and len(data['messages']) > 0 else None
    temperature = data.get('temperature')
    max_tokens = data.get('max_tokens')

    # Print received parameters
    print(f"Model: {model}")
    print(f"Prompt: {prompt}")
    print(f"Temperature: {temperature}")
    print(f"Max Tokens: {max_tokens}")

    if prompt is None:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Call OpenAI API and print call status
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        print("API call successful, response received.")
        
        # Print response content
        print("Response:", response.choices[0].text)
        
        return jsonify({'output': response.choices[0].text})
    except Exception as e:
        # Print exception information
        print(f"Error during API call: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    cuhk_account = data.get('cuhk_account')

    # Validate that the CUHK account is a 10-digit number
    if cuhk_account and len(cuhk_account) == 10 and cuhk_account.isdigit():
        try:
            # Save the valid CUHK account to a text file
            with open('cuhk_accounts.txt', 'a') as file:
                file.write(cuhk_account + '\n')
            return jsonify({'message': 'Registration successful!'})
        except Exception as e:
            return jsonify({'error': f'Failed to save account: {str(e)}'}), 500
    else:
        return jsonify({'message': 'Invalid CUHK account. Please enter a 10-digit number.'}), 400

def handle_exit(sig, frame):
    print("Shutting down server...")
    sys.exit(0)

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if __name__ == '__main__':
    # Set up signal handling to ensure proper shutdown
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    # Start with port 5000 and try subsequent ports if in use
    port = 5000
    while is_port_in_use(port):
        print(f"Port {port} is in use, trying next port...")
        port += 1

    app.run(host='0.0.0.0', port=port)
