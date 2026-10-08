import requests

# Call the API
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Check the response status code
if response.status_code == 200:
    # Convert response to JSON
    users = response.json()

    # Display user names
    print("User Names:")

    for user in users:
        print(user["name"])
else:
    print("Failed to fetch users.")
    print("Status Code:", response.status_code)