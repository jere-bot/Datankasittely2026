# TODO:
# Import pandas library
# Import fetch_data from client.api_client
# Import validate_items from utils.validators
# In the main function:
#   - fetch items from the API using the fetch_data function
#   - validate the received items using the vas lidate_itemfunction, which returns True if the items are valid, otherwise raises a ValueError with an appropriate message
#   - write the valid items to a dataframe using pandas, and then save the dataframe to a JSON file named "data/posts.json"

import pandas as pd
from utils.validators import validate_items
from client.api_client import fetch_data

def main():

    api_url = "https://jsonplaceholder.typicode.com/posts"

    print("Fetching paginated data…")
    # Fetch items
    data = fetch_data(api_url)
    if data is None:
        return

    print("Validating items…")
    # Validate items
    validData = validate_items(data)
    

    json_file_path = "data/posts.json"
    # Save JSON data into the file
    if validData:
        df = pd.DataFrame(data).to_json(json_file_path)
        
    else:
        print("Data not valid.")

if __name__ == "__main__":
    main()