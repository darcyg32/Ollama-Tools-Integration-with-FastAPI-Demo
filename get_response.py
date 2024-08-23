import requests
from tools import tools
from functions import FUNCTION_REGISTRY

# Function to send a request to the FastAPI server
def send_request(messages):
    url = "http://localhost:8000/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
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

# Function to process tool calls and return the results
def process_tool_calls(tool_calls):
    results = []
    available_functions = FUNCTION_REGISTRY

    for tool in tool_calls:
        function_name = tool['function']['name']
        function_args = tool['function']['arguments']
        
        # Get the function from the registry
        func = available_functions.get(function_name)
        
        if func:
            try:
                # Call the function with the provided arguments
                result = func(**function_args)
                results.append(result)
            except TypeError as e:
                results.append(f"Error calling {function_name}: {e}")
        else:
            results.append(f"Function {function_name} not found in registry")

    return results

# Entry point of the script when run from the command line
if __name__ == "__main__":
    # Init system conversation (Room for improvement here)
    messages = [{'role': 'system', 'content': 'You are a chatbot assistant with access to a tool to get the current weather in a specified city, and to get the current time for the user. If you do not have the right tool to answer the user, you may attempt provide an answer without one. You do not need to mention your tools to the user.'}]
    
    # Append user prompt
    messages.append({'role': 'user', 'content': 'Hi, nice to meet you. How are you? By the way, do you know the weather in London at the moment. Also, what time is it for me right now?'})

    # First API call, send the query and function description to the model
    response = send_request(messages)

    # Add the model's response to the conversation history
    messages.append(response['message'])
    
    # Process function calls made by the model
    if response['message'].get('tool_calls'):
        tool_calls = response['message']['tool_calls']
        results = process_tool_calls(tool_calls)

        # Add function results to the conversation
        for result in results:
            messages.append({
                'role': 'tool',
                'content': result
            })

    # Second API call: Get final response from model
    final_response = send_request(messages)

    # Print response
    print(final_response['message']['content'])    