import requests
import json
import ollama

OLLAMA_URL = "http://localhost:11434"

def test_ollama_chat():
    payload = {
        "model": "qwen2:7b",
        "messages": [{"role": "user", "content": "Give me a receipe for a chocolate cake."}],
        "temperature": 0.7
    }
    response = requests.post(f"{OLLAMA_URL}/api/chat", json=payload, stream=True)
    if response.status_code == 200:
        print("LLM Response:")
        for line in response.iter_lines(decode_unicode=True):
            if line: #Ignore empty lines
                try:
                    # Parse each line as JSON
                    data = json.loads(line)
                    # extract and print the content
                    if "message" in data and "content" in data["message"]:
                        print(data["message"]["content"], end="")
                except json.JSONDecodeError:
                    # Handle the case where the line is not valid JSON
                    print("Error decoding JSON:", line)
        print()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def ollama_package():
    # Initialize the Ollama client
    client = ollama.Client()

    # Define the model and the input prompt
    model = "qwen2:7b"  # Replace with your model name
    prompt = "What is Python?"

    # Send the query to the model
    response = client.generate(model=model, prompt=prompt)

    # Print the response from the model
    print("Response from Ollama:")
    print(response.response)

if __name__ == "__main__":
    test_ollama_chat()
    # ollama_package()