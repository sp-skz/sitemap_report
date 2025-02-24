import pandas as pd
from tqdm import tqdm
tqdm.pandas()
from src.check_url_status import check_url_status
from src.get_sitemaps_urls import get_sitemaps_urls
from src.get_folders import get_folders
from src.create_excel import crearte_excel

############### SETING VARIABLES  ###############

sitemap = "https://wecamp.net/sitemap.xml"
domain = "https://wecamp.net/"
root_language = 'es'
project_name = 'WECAMP_WCP'

#################################################

def main():

    df = get_sitemaps_urls(sitemap)
    df[["status_code", "indexable"]] = df["url"].progress_apply(lambda url: pd.Series(check_url_status(url)))
    df = get_folders(df, domain, root_language)
    crearte_excel(df, project_name)
    
if __name__ == "__main__":
    main()
