import requests
import json
import sys
from tools import tools

# Function to send a request to the FastAPI server
def send_request(model, prompt):
    # Determine the URL based on whether a formatted response is requested
    url = "http://localhost:8000/chat"
    headers = {"Content-Type": "application/json"}  # Specify the content type as JSON
    data = {
        "model": model,     # Model name to be used
        "prompt": prompt,   # Prompt to be sent to the model
        "stream": False,     # Streaming flag
        "tools": tools
    }

    # Send a POST request to the appropriate FastAPI endpoint
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)

    # Handle the response based on the status code
    if response.status_code == 200:
        # Stream and print each line of the response
        for line in response.iter_lines():
            if line:
                print(line.decode('utf-8'))
    else:
        # Print an error message if the request failed
        print(f"Error: {response.status_code} - {response.text}")

# Entry point of the script when run from the command line
if __name__ == "__main__":
    # Check if the required args are provided
    if len(sys.argv) < 2:
        print("Usage: python send_request.py <model> <prompt>")
        sys.exit(1)

    # Extract coommand line args
    model = sys.argv[1]
    prompt = sys.argv[2]

    # Call the function to send the request
    send_request(model, prompt)
