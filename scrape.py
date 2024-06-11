# scrape.py

import sys
import json

# Read the incoming data from stdin
input_data = sys.stdin.read()

# Parse the input JSON data
data = json.loads(input_data)

# Get the content from the JSON data
content = data['content']

# Print the content (or process it further as needed)
print(f"Received content from index.html: {content}")
