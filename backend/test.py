import os
import json
from google.oauth2 import id_token
import requests

# Load the JSON data
json_data = '''
{
  "credential": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjZmOTc3N2E2ODU5MDc3OThlZjc5NDA2MmMwMGI2NWQ2NmMyNDBiMWIiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI1MzAyNzQzNTU1ODQtNWo1bHUycTNlOWZwbnMxdGVjNDFmYjhpN2MxNXBqZ2wuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI1MzAyNzQzNTU1ODQtNWo1bHUycTNlOWZwbnMxdGVjNDFmYjhpN2MxNXBqZ2wuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJnaXZlbl9uYW1lIjoiQkVXSU4gRkVMSVggUiBBIiwiZmFtaWx5X25hbWUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLRDVuSmowc2lEZWxONzR2TXV6ZE14Wjh4UFNWeUx3UWluYWtUV2VkV3g9czk2LWMiLCJnaXZlbl9uYW1lIjoiQkVXSU4gRkVMSVggUiBBIiwiZmFtaWx5X25hbWUiOiJVUksyMUNTMTEyOCIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNzA5Mzg4NTg2LCJleHAiOjE3MDkzOTIxODYsImp0aSI6Ijg1MmQ1ZmZmOTJmNzA0ZGZjOWE3MjcwZjZkNzFkMDAwMDQwYjM1OGUifQ.K0NJt-OI54PS3BMvNTBYTcsDMU604LzGAp4",
  "clientId": "530274355584-5j5lu2q3e9fpns1tec41fb8i7c15pjgl.apps.googleusercontent.com",
  "select_by": "btn"
}
'''

# Parse the JSON data
data = json.loads(json_data)

# Extract the ID token and client ID from the JSON data
token = data['credential']
client_id = data['clientId']

# Verify the ID token
try:
    # Get the Google ID token info
    id_info = id_token.verify_oauth2_token(token, requests.Request(), client_id)
    print(json.dumps(id_info, indent=4))

except ValueError as e:
    print(e)