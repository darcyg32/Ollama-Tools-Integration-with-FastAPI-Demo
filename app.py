from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import requests
from utils import post_request_and_process_response

# Initialize FastAPI application
app = FastAPI()

# Define a data model using Pydantic for the request body
class GenerateRequest(BaseModel):
    model: str = "llama3.1" # Name of the model to be used
    prompt: str             # Prompt to be sent to the model
    stream: bool = False    # Flag to enable streaming of responses
    tools: list             # List of provided tools

# Define endpoint to handle requests and return the full raw JSON response
@app.post("/chat")
async def generate_full(request: GenerateRequest):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": request.model,
        "messages": [
            {
                "role": "user",
                "content": request.prompt
            }
        ],
        "stream": request.stream,
        "tools": request.tools,
    }

    json_responses = post_request_and_process_response(url, headers, data, stream=True)

    return json_responses
