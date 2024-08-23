import requests
import json
import sys
from tools import tools
from utils import post_request_and_process_response

# Function to send a request to the FastAPI server
def send_request(prompt):
    url = "http://localhost:8000/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False,
        "tools": tools
    }

    json_responses = post_request_and_process_response(url, headers, data, stream=True)
    
    # Print the entire response
    for response in json_responses:
        print(response)

# Entry point of the script when run from the command line
if __name__ == "__main__":
    # Check if the required args are provided
    if len(sys.argv) < 1:
        print("Usage: python send_request.py <prompt>")
        sys.exit(1)

    # Extract coommand line args
    prompt = sys.argv[1]

    # Call the function to send the request
    send_request(prompt)
