import requests
from bs4 import BeautifulSoup

def scrape_facebook_page(username: str):
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "page_name": soup.find("title").text.strip(),
        "page_url": url,
        "profile_pic": extract_profile_pic(soup),
        "total_followers": extract_followers(soup),
        "total_likes": extract_likes(soup),
        "page_category": extract_category(soup),
        "page_creation_date": extract_creation_date(soup),
        "email": extract_email(soup),
        "website": extract_website(soup),
        "posts": scrape_posts(username),
        "followers": scrape_followers(username)
    }
    return data

def extract_profile_pic(soup):
    return soup.find("meta", property="og:image")["content"] if soup.find("meta", property="og:image") else ""

def extract_followers(soup):
    return soup.find("meta", property="og:followers")["content"] if soup.find("meta", property="og:followers") else "0"

def extract_likes(soup):
    return soup.find("meta", property="og:likes")["content"] if soup.find("meta", property="og:likes") else "0"

def extract_category(soup):
    return soup.find("meta", property="og:category")["content"] if soup.find("meta", property="og:category") else "Unknown"

def extract_creation_date(soup):
    return soup.find("meta", property="og:created_time")["content"] if soup.find("meta", property="og:created_time") else "Unknown"

def extract_email(soup):
    return soup.find("meta", property="og:email")["content"] if soup.find("meta", property="og:email") else "Not Available"

def extract_website(soup):
    return soup.find("meta", property="og:website")["content"] if soup.find("meta", property="og:website") else "Not Available"

def scrape_posts(username: str):
    return [{"post_id": "123", "content": "Sample Post", "likes": 100, "comments": scrape_comments("123")}]

def scrape_comments(post_id: str):
    return [{"comment_id": "456", "text": "Nice post!", "likes": 10}]

def scrape_followers(username: str):
    return [{"follower_id": "789", "name": "John Doe"}]