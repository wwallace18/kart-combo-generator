import requests
#!/usr/bin/python3
import random
import json
import os
from slack_webhook import Slack


def main():
    characters = makeList("characters.txt")
    body = makeList("body.txt")
    tires = makeList("tires.txt")
    gliders = makeList("gliders.txt")

    webhook = os.environ.get("KART_SLACK_WEBHOOK")

    choice = f"Character: {random.choice(characters)} Body: {random.choice(body)} Tire: {random.choice(tires)} Glider: {random.choice(gliders)}"

    slack = Slack(url=webhook)
    slack.post(text=choice)

def makeList(path):
    f = open(path, "r")
    lst = []
    for item in f:
        lst.append(item)
    f.close()
    return lst


if __name__ == "__main__":
    main()
