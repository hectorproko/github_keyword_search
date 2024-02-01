import requests
from termcolor import colored
import os

# Securely store your personal access token
personal_access_token = os.environ.get("GITHUB_ACCESS_TOKEN")

# Base URL for GitHub API
base_url = "https://api.github.com"
# Define the keyword to search for
keyword = "cert"
headers = {"Authorization": f"token {personal_access_token}"}

# Test the connection by getting your user information
user_url = f"{base_url}/user"
response = requests.get(user_url, headers=headers)

if response.status_code == 200:
    print("Connection successful!")
    print("Your GitHub username:", response.json()["login"])
else:
    print("Connection failed with status code:", response.status_code)


# Rest of code
    
# Get a list of your repositories
repos_url = f"{base_url}/user/repos"
headers = {"Authorization": f"token {personal_access_token}"}
response = requests.get(repos_url, headers=headers)
repos = response.json()

# Iterate through each repository and search its contents
for repo in repos:
    repo_name = repo["name"]
    print(repo_name)
    contents_url = f"{base_url}/repos/{repo['owner']['login']}/{repo['name']}/contents"
    #print(contents_url)
    response = requests.get(contents_url, headers=headers)
    contents = response.json()

    for file in contents:
        if file["type"] == "file":
            file_url = file["download_url"]
            #print(file_url)
            if file_url is not None:
                response = requests.get(file_url, headers=headers)
                #print(response)
                file_contents = response.text
                if keyword in file_contents:
                    #print(colored(f"Keyword found in {repo_name}/{file['path']}", "green"))
                    print(colored(f"Keyword found in {file['path']}", "green"))
            else:
                print("\033[91mInvalid URL or URL is None\033[0m")
                


            
            #if "_links" in file and "git" in file["_links"] and "tree" in file["_links"]["git"]:
            #    contents_url = file["_links"]["git"]["tree"]
            #else:
            #    contents_url = None