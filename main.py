from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Directly set your API key here (not secure for production!)
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"  # only if you use openrouter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({'reply': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
