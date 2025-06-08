# 🤖 ChatBot

A simple Python-based chatbot built with Flask and deployed on Render.

🌐 **Live URL**: [Chatbot Link](https://chatbot-3-ideb.onrender.com)

---

## 📝 Features

- Accepts POST requests with user input
- Returns bot-generated responses
- Lightweight and beginner-friendly
- Deployed on [Render](https://render.com)

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- `pip`
- `Flask`
- `gunicorn` (for deployment)

---

## 📁 Project Structure

\`\`\`
chatbot/
├── main.py
├── requirements.txt
├── Procfile
└── README.md
\`\`\`

---

## ⚙️ Installation & Running Locally

1. **Clone the repo**
\`\`\`bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
\`\`\`

2. **Create a virtual environment**
\`\`\`bash
python -m venv venv
source venv/bin/activate
\`\`\`

3. **Install dependencies**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. **Run the app**
\`\`\`bash
python main.py
\`\`\`

By default, the app runs on \`http://127.0.0.1:5000\`.

---

## 📡 API Usage

### Endpoint
\`\`\`
POST /api/chat
\`\`\`

### Request Body (JSON)
\`\`\`json
{
  "message": "Hello"
}
\`\`\`

### Response (JSON)
\`\`\`json
{
  "response": "You said: Hello"
}
\`\`\`

Test it using [Postman](https://www.postman.com/) or \`curl\`:

\`\`\`bash
curl -X POST https://chatbot-j596.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
\`\`\`

---

## 🛠 Deployment (on Render)

1. Push code to GitHub
2. Create a new **Web Service** on Render
3. Use the following settings:

- **Build Command**: \`pip install -r requirements.txt\`
- **Start Command**: \`gunicorn main:app\`
- **Environment**: Python 3.8 or higher
- **Port**: Automatically handled by Render (use \`host="0.0.0.0"\` in Flask)

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Made with ❤️ by [Hamidur Rahman](https://github.com/hamidur0x)
