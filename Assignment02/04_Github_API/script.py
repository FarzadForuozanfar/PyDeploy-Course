import requests

url = "https://api.github.com/users/FarzadForuozanfar"
response = requests.get(url)

print(f"Followings: {response.json()['following']}, Followers: {response.json()['followers']}")
