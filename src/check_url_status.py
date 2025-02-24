from bs4 import BeautifulSoup
import httpx

def check_url_status(url):
    """Fetch URL status, redirection (301/302), and indexability (meta robots noindex)."""
    try:
        response = httpx.get(url, follow_redirects=False, timeout=5)
        status_code = response.status_code
        indexable = True  # Default: Assume indexable
        if status_code == 200:  # Only check for indexability if page loads correctly
            soup = BeautifulSoup(response.text, "html.parser")
            meta_robots = soup.find("meta", attrs={"name": "robots"})
            if meta_robots and "noindex" in meta_robots.get("content", "").lower():
                indexable = False
        else:
            indexable = False
        return status_code, indexable

    except Exception:
        return "Error", False