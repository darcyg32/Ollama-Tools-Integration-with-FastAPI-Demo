from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

# Initialize FastAPI application
app = FastAPI()

# Define a data model using Pydantic for the request body
class ChatRequest(BaseModel):
    model: str = "llama3.1"  # Name of the model to be used (placeholder llama3.1)
    stream: bool = False     # Flag to enable streaming of responses
    tools: list              # List of tools that the model has access to for fulfilling requests
    messages: list           # List of messages forming the conversation context

# Define a POST endpoint to handle incoming chat requests
@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Handles incoming chat requests, forwards them to the model server, and returns the response.

    Args:
        request (ChatRequest): A request object containing the model name, streaming flag,
                               tools, and conversation history.

    Returns:
        JSON: The full response from the model server as a JSON object.
    """
    # URL of the model server to forward the request to
    url = "http://ollama:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": request.model,
        "messages": request.messages,
        "stream": request.stream,
        "tools": request.tools,
    }

    try:
        # Send the request to the model server and get the response
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception if the response contains an HTTP error
    except requests.exceptions.RequestException as e:
        # If an error occurs during the request, raise an HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail=f"Request failed: {e}")
    
    # Return the model server's JSON response directly to the client
    
    return response.json()
