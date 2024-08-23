import requests
import json
import sys
from tools import tools, extract_function_details

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

    response = requests.post(url, headers=headers, json=data)  # Use 'json=data' instead of 'data=json.dumps(data)'
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the response JSON if successful
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Entry point of the script when run from the command line
if __name__ == "__main__":
    # Check if the required args are provided
    if len(sys.argv) < 2:  # The prompt is expected to be the second argument
        print("Usage: python get_response.py <prompt>")
        sys.exit(1)

    # Extract command line args
    prompt = sys.argv[1]

    # Call the function to send the request
    response = send_request(prompt)
    
    # Print the full JSON response
    print("Full Response:")
    print(json.dumps(response, indent=2))  # Pretty-print the full JSON response

    # Extract and print function details
    function_details = extract_function_details(response)
    print("\nExtracted Function Details:")
    print(json.dumps(function_details, indent=2))  # Pretty-print the extracted function details
