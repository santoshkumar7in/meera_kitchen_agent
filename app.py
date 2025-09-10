# app.py
from flask import Flask, request, jsonify
from agent import CustomAIAgent
import os

app = Flask(__name__)

# Initialize agent
agent = CustomAIAgent("You are a helpful customer service assistant")

@app.route('/')
def home():
    return jsonify({
        "message": "AI Agent API is running!",
        "endpoints": {
            "/chat": "POST - Send message to agent",
            "/reset": "POST - Reset conversation"
        }
    })


@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
            
        response = agent.chat(user_message)
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset_endpoint():
    agent.reset_conversation()
    return jsonify({'status': 'Conversation reset'})

if __name__ == '__main__':
    print("Starting AI Agent Server...")
    print("Access the API at: http://localhost:5000")
    app.run(debug=True, port=5000, host='0.0.0.0')