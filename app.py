from flask import Flask, request
from flask_cors import CORS
from g4f import ChatCompletion

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173', 'https://gpt4free-flask-vercel.vercel.app'])


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    response = ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": data['message']}],
        stream=True,
    )
    return {'response': list(response)}
