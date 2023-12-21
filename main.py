import requests
from logger import Logger
from random import randint
import time


def get_true(url, headers, num):
     response = requests.get(url, headers=headers)
     time.sleep(0.72)
     if len(response.json()) >= num:
         return True
     else:
         return False



def get_github_users(token):
    
     users = []
     # Set headers for request using access token
     headers = {
         "Authorization": f"Bearer {token}",
         "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28"
     }

     for i in range(10000):
         since = randint(100, 154_000_000)
         print(i, since)
         # Endpoint URL to get a list of users
         endpoint = f'https://api.github.com/users?per_page=100&since={since}'

         # Execute the request
         response = requests.get(endpoint, headers=headers)
         time.sleep(0.72)
         # Check the success of the request
         if response.status_code == 200:
             # Return data in JSON format
             for user in response.json():
                 followers_url = user['followers_url']
                 repos_url = user['repos_url']
                 if user['type'] == "User" and user['site_admin'] == False:
                     if get_true(followers_url, headers, 5):# and get_true(repos_url, headers, 2):
                         user_data = [user.get('login', ''), user.get('node_id', ''), user.get('html_url', ''), user.get('followers_url', '') , user.get('repos_url', '')]
                         print(user_data)
                         for item in user_data:
                             log.updater(user['id'], item)
                         log.write('GH_users.csv')
         else:
             # Display an error message
             print(f"Error: {response.status_code}, {response.text}")


log = Logger('GH_users.csv')

# Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
github_token = 'YOUR_GITHUB_TOKEN'
users = get_github_users(github_token)
