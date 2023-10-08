import requests

def make_request():
    """Make request to Optimal website"""
    url = "https://optimal-capstone-app.onrender.com/"

    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully pinged Optimal website.")
    else:
        print("Ping to Optimal unsuccessful.")