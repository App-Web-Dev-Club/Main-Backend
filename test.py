import jwt
import requests

client_id = "530274355584-5j5lu2q3e9fpns1tec41fb8i7c15pjgl.apps.googleusercontent.com"
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjFmNDBmMGE4ZWYzZDg4MDk3OGRjODJmMjVjM2VjMzE3YzZhNWI3ODEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI1MzAyNzQzNTU1ODQtNWo1bHUycTNlOWZwbnMxdGVjNDFmYjhpN2MxNXBqZ2wuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI1MzAyNzQzNTU1ODQtNWo1bHUycTNlOWZwbnMxdGVjNDFmYjhpN2MxNXBqZ2wuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDU5MDE2MjI0ODEyODQyNzc1NzEiLCJlbWFpbCI6ImJpd2luZmVsaXhAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTcwNTQ4Nzg2NSwibmFtZSI6IkJld2luIEZlbGl4IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0l2UjNoMXh5LU1tSENNa3FhR0pwdXN0YVhCU0MxVEprUHhhaVJWR3RibWtDMD1zOTYtYyIsImdpdmVuX25hbWUiOiJCZXdpbiIsImZhbWlseV9uYW1lIjoiRmVsaXgiLCJsb2NhbGUiOiJlbiIsImlhdCI6MTcwNTQ4ODE2NSwiZXhwIjoxNzA1NDkxNzY1LCJqdGkiOiI5NzEwOTFhNjA3MmVmYmY4MDU1MmFhM2JkNmFkODA0YmViMTBhYzVmIn0.EAnkYV5rDSdg87qLmBQhNh5bDjKFj1_zdppg7BYWdnKkditJM0ErqjXNb3JOq0RhsP9zuF_WdOtxWYwLHSrcrRw0vo4TGMMw57m5EeYn912lyAmsqxOdJbJ6e5q6IoqjW20q9tnLXUT2b8WKw0HfO1S7iSI5tiQHKIx-KhPZwq1SK11-UN2729VCuZqU-l936Gn2gsEym0joaVdr6o528ej27GvwlMtOi5SKORcTXpPS2ivmupuwChzmJC0bOxlOUuun4gJTYiNbgfMEkhB_7SKN86LDkkHpR0jXy61Eup-m63J17jomPzTjPN3KNbHr54BtsrWmNk2Ddr0XRisZVw"

decoded_token = jwt.decode(token, verify=False)  # Set verify=False to skip signature verification

# Validate claims
if decoded_token['aud'] != client_id:
    print("Invalid audience (client_id)")
    # Handle the error or raise an exception

# You can add additional checks for 'iss', 'exp', etc.

print(decoded_token)