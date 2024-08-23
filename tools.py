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