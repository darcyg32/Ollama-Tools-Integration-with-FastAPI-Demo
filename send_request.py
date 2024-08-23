import requests
from tools import tools
from functions import FUNCTION_REGISTRY

def send_request(messages):
    """
    Sends a request to the FastAPI server and returns the response.

    Args:
        messages (list): A list of messages representing the conversation history to be sent to the model.

    Returns:
        dict: The response from the server as a dictionary, or an error message if the request fails.
    """
    url = "http://localhost:8000/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
        "stream": False,
        "tools": tools,
        "messages": messages
    }

    try:
        # Send the request to the FastAPI server and get the response
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception if the response contains an HTTP error
        return response.json()  # Return the response JSON if the request was successful
    except requests.exceptions.RequestException as e:
        # Return an error message if the request fails due to network issues or server errors
        return {"error": f"Request failed: {e}"}

# Function to process tool calls and return the results
def process_tool_calls(tool_calls):
    """
    Processes tool calls made by the model, invokes the corresponding functions, and returns their results.

    Args:
        tool_calls (list): A list of tool call dictionaries, where each dictionary specifies the function name
                           and arguments to be used.

    Returns:
        list: A list of results from each tool call, including any errors encountered during processing.
    """
    results = []  # List to store results of tool calls
    available_functions = FUNCTION_REGISTRY # Get list of available functions from the function registry

    # Iterate over each tool call made by the model
    for tool in tool_calls:
        function_name = tool['function']['name']        # Extract the function name from the tool call
        function_args = tool['function']['arguments']   # Extract the function arguments from the tool call
        func = available_functions.get(function_name)   # Look up the function by name in the registry
        
        if func:
            try:
                # Call the function with the provided arguments and store the result
                result = func(**function_args)
                results.append(result)
            except TypeError as e:
                # Append an error message if there is a problem with the function call
                results.append(f"Error calling {function_name}: {e}")
        else:
            # Append an error message if the function is not found in the registry
            results.append(f"Function {function_name} not found in registry")

    return results # Return the list of results (or errors)

if __name__ == "__main__":
    # Initialize the conversation with a system message (Room for improvement here)
    messages = [
        {
            'role': 'system',
            'content': (
                'You are a chatbot assistant with access to a tool to get the current weather in a specified city, '
                'and to a tool to get the current time for the user. Sometimes your tools may not work, this does not '
                'mean that all your tools are not working. One tool could have be temporarily out of service. Although '
                'normally not needed, you can use multiple tools in combination with each other if you think that is best. '
                'Sometimes you will need to use both tools, sometimes you will only need to use one, and sometimes you will '
                'not need to use any. If you do not have the right tool to answer the user, you may attempt provide an answer '
                'without one. You do not need to mention your tools to the user.'
            )
        }
    ]

    # Append the user's initial message to the conversation
    messages.append({'role': 'user', 'content': 'Hi, how are you? What time is it? Also, what is the weather in Madrid?'})

    # First API call: Send the initial conversation to the model and get its response
    response = send_request(messages)

    # Add the model's response to the conversation history
    messages.append(response['message'])
    
    # Check if the model made any tool calls (requests to execute functions)
    if response['message'].get('tool_calls'):
        tool_calls = response['message']['tool_calls']
        results = process_tool_calls(tool_calls) # Process each tool call and get the results

        # Add the results of tool calls to the conversation history
        for result in results:
            messages.append({'role': 'tool', 'content': result})

    # Second API call: Send the updated conversation (including tool call results) to the model
    final_response = send_request(messages)

    # Print the model's final response to the console
    print(final_response['message']['content'])    