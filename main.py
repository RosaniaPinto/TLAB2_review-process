from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: list):
    with open(filepath, "r") as f:
        data = json.load(f)
    print(data["results"])

    reviews = data

    sentiments = [get_sentiment(list")] for list in revioews
                                
    make_plot(sentiments)

    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
