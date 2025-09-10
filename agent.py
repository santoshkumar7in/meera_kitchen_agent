# agent.py
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CustomAIAgent:
    def __init__(self, system_prompt="You are a helpful assistant"):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.client = openai.OpenAI(api_key=api_key)
        self.system_prompt = system_prompt
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
    
    def chat(self, user_message):
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Get response from OpenAI
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.conversation_history,
            temperature=0.7
        )
        
        # Extract and store AI response
        ai_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": ai_response})
        
        return ai_response
    
    def reset_conversation(self):
        self.conversation_history = [
            {"role": "system", "content": self.system_prompt}
        ]

# Test the agent
if __name__ == "__main__":
    try:
        agent = CustomAIAgent("You are a friendly assistant")
        response = agent.chat("Hello! What can you help me with?")
        print("Agent Response:", response)
        print("\nConversation History:")
        for msg in agent.conversation_history:
            print(f"{msg['role']}: {msg['content']}")
    except Exception as e: 
        print(f"Error: {e}")