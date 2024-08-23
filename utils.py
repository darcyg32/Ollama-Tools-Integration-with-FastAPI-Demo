import requests
import json

def post_request_and_process_response(url, headers, data, stream=True):
    # Send a POST request to the model API
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=stream)
    
    # Handle the response based on the status code
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    
    # Capture and process the response
    json_responses = []
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            try:
                parsed_json = json.loads(decoded_line)
                json_responses.append(parsed_json)  # Store the JSON object
            except json.JSONDecodeError:
                continue  # Skip lines that aren't valid JSON
    
    return json_responses
