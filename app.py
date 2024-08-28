from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS support

# Replace with your API key and base URL if needed
api_key = 'sk-5pkp7lLRC2nx8hCzBfB44fD499Bf48B3B408Eb39E604Fa77'
base_url = 'https://oneapi.xty.app/v1'

openai.api_key = api_key
openai.api_base = base_url

@app.route('/generate', methods=['POST'])
def generate():
    # Print request data for debugging
    print("Received request data:", request.json)
    
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')
    temperature = data.get('temperature')
    max_tokens = data.get('max_tokens')

    # Print received parameters
    print(f"Model: {model}")
    print(f"Prompt: {prompt}")
    print(f"Temperature: {temperature}")
    print(f"Max Tokens: {max_tokens}")

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
