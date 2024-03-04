import requests
import urllib
import jwt
import os

from oauth2client import client

# Load environment variables from .env file

def get_id_token_with_code_method_1(code):
    redirect_uri = "postmessage"
    token_endpoint = "https://oauth2.googleapis.com/token"
    payload = {
        'code': code,
        'client_id': '993704372764-mle990a1g3a6kjve49g0ohu6ng7qkmcu.apps.googleusercontent.com',
        'client_secret': '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',
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    body = urllib.parse.urlencode(payload)
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    response = requests.post(token_endpoint, data=body, headers=headers)
    if response.ok:
        id_token = response.json()['id_token']
        print(id_token)
        return jwt.decode(id_token, options={"verify_signature": False})
    else:
        print(response.json())
        return None


def get_id_token_with_code_method_2(code):
    CLIENT_SECRET_FILE = r'E:\Attendanance\backend\backend\client_secret_993704372764-mle990a1g3a6kjve49g0ohu6ng7qkmcu.apps.googleusercontent.com.json'
    # Exchange auth code for access token, refresh token, and ID token
    credentials = client.credentials_from_clientsecrets_and_code(
        CLIENT_SECRET_FILE,
        ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid', 'email', 'profile'],
        code
    )


    # print(credentials)
    
    return credentials.id_token