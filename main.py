from fastapi import FastAPI, Query
from scraper import scrape_facebook_page
from dp import (
    save_page_data, get_page_data, get_recent_posts,
    get_followers, filter_pages_by_followers, filter_pages_by_name, filter_pages_by_category
)

app = FastAPI()

@app.get("/page/{username}")
def get_page(username: str):
    data = get_page_data(username)
    if not data:
        data = scrape_facebook_page(username)
        if data:
            save_page_data(data)
    return data

@app.get("/page/{username}/posts")
def get_posts(username: str, limit: int = 10):
    return get_recent_posts(username, limit)

@app.get("/page/{username}/followers")
def get_followers_api(username: str, limit: int = 10, page: int = 1):
    return get_followers(username, limit, page)

@app.get("/pages/filter")
def filter_pages(
    min_followers: int = Query(0),
    max_followers: int = Query(1000000),
    name: str = Query(None),
    category: str = Query(None)
):
    if name:
        return filter_pages_by_name(name)
    elif category:
        return filter_pages_by_category(category)
    return filter_pages_by_followers(min_followers, max_followers)