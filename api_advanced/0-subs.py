import requests

def number_of_subscribers(subreddit):
    # URL of the Reddit API endpoint to get subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomBot/1.0'}
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is OK (200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Get the number of subscribers from the response
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 302:
        # Redirect response, indicating an invalid subreddit
        return 0
    else:
        # Other errors
        print("Error:", response.status_code)
        return 0

# Test the function
subreddit = "python"
print("Number of subscribers:", number_of_subscribers(subreddit))

