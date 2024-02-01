import requests

personal_access_token = "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"
base_url = "https://api.github.com"

headers = {"Authorization": f"token {personal_access_token}"}

# Test the connection by getting your user information
user_url = f"{base_url}/user"
response = requests.get(user_url, headers=headers)

if response.status_code == 200:
    print("Connection successful!")
    print("Your GitHub username:", response.json()["login"])
else:
    print("Connection failed with status code:", response.status_code)


