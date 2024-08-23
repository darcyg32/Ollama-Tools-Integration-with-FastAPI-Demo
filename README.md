# Tool Integration with Ollama and FastAPI Demo

This project demonstrates how to integrate tools with Ollama in a FastAPI application. It showcases three main functionalities:
- **Weather Tool**: Get the current temperature for a specified city.
- **Time Tool**: Retrieve the current time in HH:MM:SS format.
- **Chat Interface**: Communicate with a chatbot that can utilize these tools to answer queries.

## Files
- **app.py**: Defines a FastAPI application with endpoints for generating chat responses from the Ollama API.
- **send_request.py**: A script to interact with the FastAPI application. Demonstrates how to interact with the chatbot, handle its responses, and process tool calls in a sequential conversation.
- **functions.py**: Contains the core functions that provide the weather and time data.
- **tools.py**: Defines the available tools that the chatbot can use in the appropriate format.

## Dependencies
### Required Software
- **Python**: Ensure you have Python 3.7 or later installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Requests**: A simple HTTP library for Python.
- **Ollama**: A tool for running AI models locally.

### Installation
1. **FastAPI and Requests**:
    You can install FastAPI and Requests using pip:
    `pip install fastapi requests`
    
2. **Ollama**:
    Follow the instructions on the [Ollama GitHub repository](https://github.com/ollama/ollama) to install Ollama. Make sure to download and install the version that includes the `llama3.1` model.
    
    For a quick installation via the command line, use:
    `pip install ollama`
    Ensure that you have the `llama3.1` model available. You can usually download and install it through Ollama’s CLI or the web interface.

## Usage
### Clone the Repository:
```sh
git clone [https://github.com/darcyg32/ollama-tools-project](https://github.com/darcyg32/Ollama-Tools-Integration-with-FastAPI-Demo)
cd Ollama-Tools-Integration-with-FastAPI-Demo
```
### Set Up a Virtual Environment:

### Install Dependencies:

### Running the FastAPI Server

### Sending Requests
**Using the Command-Line Script**:
    You can use `send_request.py` to interact with the FastAPI server. Here’s how to use it:
    `python send_request.py`
    - You can customize the initial system instructions at the `# Initialize the conversation with a system message` comment.
    - You can customize the initial customer message at the `# Append the user's initial message to the conversation` comment.
    
## Additional Notes
- Ensure that Ollama is properly configured and running locally on `http://localhost:11434`. Update the URL in `app.py` if your Ollama instance is hosted elsewhere.
- The FastAPI server and Ollama must be running simultaneously to process requests successfully.
- For more details on FastAPI and Requests, refer to their respective documentation:
    - [FastAPI Documentation](https://fastapi.tiangolo.com/)
    - [Requests Documentation](https://requests.readthedocs.io/en/latest/)

## System Specifications
For reference, this project was developed and tested on the following hardware:
- Processor: AMD Ryzen 5 5600X 6-Core
- GPU: NVIDIA GeForce RTX 3060 Ti
- RAM: 32 GB
- Operating System: Ubuntu/WSL on Windows 11
- Storage: 2 TB SSD
- These specifications were sufficient for running the Ollama tools integration FastAPI application demo. If you encounter any performance issues or have different specifications, you may need to adjust your setup accordingly.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
