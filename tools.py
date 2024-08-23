# Tool signatures formatted for ollama
tools = [
    {
      'type': 'function',
      'function': {
        'name': 'get_current_weather',
        'description': 'Fetch the current weather for a specified city.',
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
        'name': 'get_current_time',
        'description': 'Fetch the current time for the user.',
        'parameters': {
          'type': 'object',
          'properties': {},
          'required': [],
        },
      },
    }
]