import requests
import ecdsa
import base64
import json

url = "http://nova-hub.ru:9999/bank/get_client_ip/"  # Replace with the correct URL of your FastAPI server

# Load the private key for signing (in practice, this should be stored securely)
with open("private_key.pem", "rb") as f:
    sk = ecdsa.SigningKey.from_pem(f.read().decode('utf-8'))

# Data to be sent (could be any JSON data)
data = {"message": "This is a secure request"}  # Convert data to a Python dictionary

# Convert data to a JSON string
data_json = json.dumps(data)
# Sign the data using the private key
signature = sk.sign(data_json.encode())  # Encode data as bytes
# Base64 encode the binary signature
signature_base64 = base64.b64encode(signature)

# Prepare the request headers to include the signature and user ID (if required)
headers = {
    "X-Signature": signature_base64.decode(),  # Decode to convert bytes to a string
    "X-User-ID": "user1"  # This can be a unique identifier for the user, or any user-specific information you need
}

# Send the POST request to the server with JSON data and proper headers
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.status_code)
print(response.json())
