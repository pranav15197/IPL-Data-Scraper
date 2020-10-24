from bs4 import BeautifulSoup
import requests
from pprint import pprint


def get_batsman_data(score_table):
    rows = score_table.find("tbody").find_all("tr")[:-1]
    batting_data = []
    for row in rows:
        data = [s.text for s in row.find_all("td")]
        if len(data) < 7:
            continue
        batting_data.append(
            {
                "name": data[0].encode("ascii", "ignore").decode("ascii"),
                "dismissal": data[1],
                "runs": int(data[2]),
                "balls": int(data[3]),
                "fours": int(data[5]),
                "sixes": int(data[6]),
            }
        )
    return batting_data


def get_bowler_data(score_table):
    rows = score_table.find("tbody").find_all("tr")[:-1]
    bowler_data = []
    for row in rows:
        data = [s.text for s in row.find_all("td")]
        if len(data) < 7:
            continue
        bowler_data.append(
            {
                "name": data[0].encode("ascii", "ignore").decode("ascii"),
                "overs": float(data[1]),
                "maidens": int(data[2]),
                "runs": int(data[3]),
                "wickets": int(data[4]),
            }
        )
    return bowler_data


def get_score_data(match_link):
    resp = requests.get(match_link)
    html_doc = resp.text
    soup = BeautifulSoup(html_doc, "html.parser")
    teams = [s.text for s in soup.find("div", class_="teams").find_all("span")]
    batting_score_tables = soup.find_all("table", class_="batsman")
    batting_data = [get_batsman_data(table) for table in batting_score_tables]
    bowler_score_tables = soup.find_all("table", class_="bowler")
    bowling_data = [get_bowler_data(table) for table in bowler_score_tables]

    return [
        {
            "team": teams[i],
            "batting": batting_data[i],
            "bowling": bowling_data[i],
        }
        for i in range(2)
    ]
