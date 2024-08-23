from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import requests

# Initialize FastAPI application
app = FastAPI()

# Define a data model using Pydantic for the request body
class GenerateRequest(BaseModel):
    model: str              # Name of the model to be used
    prompt: str             # Prompt to be sent to the model
    stream: bool = False   # Flag to enable streaming of responses
    #tools: dict             # Dict of provided tools

# Define endpoint to handle requests and return the full raw JSON response
@app.post("/generate")
async def generate_full(request: GenerateRequest):
    url = "http://localhost:11434/api/generate"     # URL of the local model API
    headers = {"Content-Type": "application/json"}  # Specify the content type as JSON
    data = {
        "model": request.model,     # Model name from the request
        "prompt": request.prompt,   # Prompt from the request
        "stream": request.stream   # Streaming flag from the request
    }

    # Send a POST request to the model API
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
    
    # Capture streamed responses line by line
    raw_response = ""
    for line in response.iter_lines():
        if line:
            raw_response += line.decode('utf-8') + "\n"     # Accumulate the response
    
    # Return the full JSON response as a string
    return raw_response

# Add one for chat