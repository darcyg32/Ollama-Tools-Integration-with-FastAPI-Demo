from functions import FUNCTION_REGISTRY

tools = [
    {
      'type': 'function',
      'function': {
        'name': 'get_current_weather',
        'description': 'Get the current weather for a city',
        'parameters': {
          'type': 'object',
          'properties': {
            'city': {
              'type': 'string',
              'description': 'The name of the city',
            },
          },
          'required': ['city'],
        },
      },
    },
    {
      'type': 'function',
      'function': {
        'name': 'get_time',
        'description': 'Get the current time',
        'parameters': {
          'type': 'object',
          'properties': {},
          'required': [],
        },
      },
    }
]

# Helper function to extract 'name' and 'arguments' from tool_calls
def extract_function_details(response):
    # Safely accessing 'tool_calls' and extracting 'name' and 'arguments'
    tool_calls = response.get('message', {}).get('tool_calls', [])
    
    function_details = []
    for tool_call in tool_calls:
        function_info = tool_call.get('function', {})
        name = function_info.get('name', 'No name found')
        arguments = function_info.get('arguments', {})
        function_details.append({'name': name, 'arguments': arguments})
    
    return function_details

def process_function_calls(function_details):
    results = []
    for detail in function_details:
        function_name = detail['name']
        arguments = detail['arguments']
        
        func = FUNCTION_REGISTRY.get(function_name)
        
        if func:
            result = func(**arguments)
            results.append(result)
    
    return results