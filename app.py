from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your API key and base URL if needed
api_key = 'sk-5pkp7lLRC2nx8hCzBfB44fD499Bf48B3B408Eb39E604Fa77'
base_url = 'https://oneapi.xty.app/v1'

openai.api_key = api_key
openai.api_base = base_url

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')
    temperature = data.get('temperature')
    max_tokens = data.get('max_tokens')
    
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return jsonify({'output': response.choices[0].text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
