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
