# TODO: 
# Import requests library
# Define fetch_data function, that takes an API URL as parameter
# Use try - except structure to
# - make a GET request to the given URL with athe requests library,
# - raise an exception if the response status code indicates an error,
# - return the response data as JSON
# - print an error message if something goes wrong with the request, and return None.

import requests
import json

def fetch_data(api_url):
    try:
       res = requests.get(api_url)
       res.raise_for_status()
       data = res.json()
       return data
    except requests.ConnectionError:
        print("Could not connect")
        return None
    except requests.exceptions.HTTPError as e:
        print("HTTP status: " + e)
        return None
    except requests.JSONDecodeError:
        print("Data not stored in JSON")
        return None