import requests
from bs4 import BeautifulSoup
import pandas as pd

def sitemap_urls(sitemap_url: str):
    """Fetch all URLs from a given sitemap (handles sitemap index iteratively)."""
    urls = []
    queue = [sitemap_url]  # Use a queue to process sitemap indexes iteratively

    while queue:
        current_sitemap = queue.pop(0)
        response = requests.get(current_sitemap)
        soup = BeautifulSoup(response.text, "xml")

        # Check if it's a sitemap index (contains <sitemap> tags)
        sitemap_tags = soup.find_all("sitemap")
        if sitemap_tags:
            for sitemap in sitemap_tags:
                loc = sitemap.find("loc").text
                queue.append(loc)  # Add to queue instead of recursive call
        else:
            # Extract page URLs from the sitemap
            urls.extend([loc.text for loc in soup.find_all("loc")])
    return urls

def get_sitemaps_urls(sitemap_url):
    urls = sitemap_urls(sitemap_url)
    df = pd.DataFrame(urls, columns=["url"])
    return df