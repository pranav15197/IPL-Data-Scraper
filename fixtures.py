from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.espncricinfo.com"
FIXTURE_URL = (
    BASE_URL + "/scores/series/8048/season/2020/indian-premier-league?view=results"
)


def get_past_scorecard_links():
    resp = requests.get(FIXTURE_URL)
    html_doc = resp.text
    soup = BeautifulSoup(html_doc, "html.parser")
    score_divs = soup.find_all("div", class_="match-score-block")
    return [
        BASE_URL
        + score_div.find_all("div", class_="match-cta-container")[0]
        .find_all("a")[0]
        .get("href")
        for score_div in score_divs
    ]
