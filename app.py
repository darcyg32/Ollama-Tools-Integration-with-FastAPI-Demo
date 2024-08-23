from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Initialize FastAPI application
app = FastAPI()

# Define a data model using Pydantic for the request body
class ChatRequest(BaseModel):
    model: str = "llama3.1"  # Name of the model to be used
    prompt: str              # Prompt to be sent to the model
    stream: bool = False     # Flag to enable streaming of responses
    tools: list              # List of provided tools

# Define an endpoint to handle requests and return the full raw JSON response
@app.post("/chat")
async def chat(request: ChatRequest):
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

    response = requests.post(url, headers=headers, json=data)  # Use 'json=data' instead of 'data=json.dumps(data)'
    
    # Return the full JSON response as a JSON object
    return response.json()
