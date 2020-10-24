import json
from pprint import pprint
from fixtures import get_past_scorecard_links
from scorecard import get_score_data


def fetch_all_data():
    past_links = get_past_scorecard_links()
    bulk_data = [get_score_data(link) for link in past_links]
    with open("db.json", "w") as f:
        pprint(bulk_data)
        json.dump(bulk_data, f)


if __name__ == "__main__":
    fetch_all_data()
