import requests
import json
import sys
from tools import tools, extract_function_details, process_function_calls, reformat_results

# Function to send a request to the FastAPI server
def send_request(prompt, messages=[]):
    url = "http://localhost:8000/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False,
        "tools": tools,
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=data)  # Use 'json=data' instead of 'data=json.dumps(data)'
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the response JSON if successful
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

init_messages = [('system', "You are an assistant with access to tools, if you do not have a tool to deal with the user's request but you think you can answer do it so, if not explain your capabilities")]

# Entry point of the script when run from the command line
if __name__ == "__main__":
    # Check if the required args are provided
    if len(sys.argv) < 2:  # The prompt is expected to be the second argument
        print("Usage: python get_response.py <prompt>")
        sys.exit(1)

    # Extract command line args
    prompt = sys.argv[1]

    messages=[{'role': role, 'content': content} for role,content in init_messages],

    # Call the function to send the request
    response = send_request(prompt, messages)
    
    # Extract function details
    function_details = extract_function_details(response)

    # Get results of function calls
    function_results = process_function_calls(function_details)
    
    # Format the results to be sent in the next request in 'messages'
    reformatted_results = reformat_results(function_results)
    print(json.dumps(reformatted_results, indent=2))