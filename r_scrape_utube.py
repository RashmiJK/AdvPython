import requests

# Replace with your YouTube Data API key
API_KEY = "<Your API Key"
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

# Function to get video links related to Greece trip
def get_youtube_links(query, max_results=50):
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': max_results,
        'key': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        video_links = []

        for item in data.get('items', []):
            video_id = item['id']['videoId']
            video_links.append(f"https://www.youtube.com/watch?v={video_id}")

        return video_links
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

# Main execution
if __name__ == "__main__":
    search_query = "Greece trip"
    video_links = get_youtube_links(search_query, max_results=50)

    if video_links:
        print("YouTube Links:")
        for link in video_links:
            print(link)
    else:
        print("No links found.")
