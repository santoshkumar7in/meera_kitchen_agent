# test_client.py
import requests
import json


def test_agent():
    base_url = "http://localhost:5000"
    
    # Test 1: Chat endpoint
    print("=== Testing Chat Endpoint ===")
    response = requests.post(
        f"{base_url}/chat",
        json={"message": "Hello! What can you help me with today?"}
    )
    
    if response.status_code == 200:
        data = response.json()
        print("Response:", data['response'])
    else:
        print("Error:", response.status_code, response.text)
    
    # Test 2: Another message to test conversation flow
    print("\n=== Testing Follow-up Message ===")
    response = requests.post(
        f"{base_url}/chat",
        json={"message": "Can you tell me a joke?"}
    )
    
    if response.status_code == 200:
        data = response.json()
        print("Response:", data['response'])
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    test_agent()