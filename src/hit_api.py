import requests
from requests.exceptions import Timeout
import click

activities = [
    "education",
    "recreational",
    "social",
    "diy",
    "charity",
    "cooking",
    "relaxation",
    "music",
    "busywork",
]


def query(subject):
    """Query the bored API to find something to do.  You
    can change which argument you pass through this method with any of the strings in
    the activities list.  Choose an activity you feel like trying something new in."""
    try:
        hit_api = requests.get(
            "http://www.boredapi.com/api/activity?type=" + subject, timeout=5
        )
    except Timeout:
        print("I waited for too long!")
    else:
        print("The API request got executed!")

        hit_api.encoding = "utf-8"
        find_key = hit_api.text
        find_key = hit_api.json()
        print(f"{subject.capitalize()} idea: {find_key['activity']}")


@click.group()
def cli():
    pass


@cli.command(name="all", help="Ask for suggestions on all categories")
def suggestion_for_each_activity():
    for every_activity in activities:
        query(every_activity)


@cli.command(name="edu", help="Ask for a random educational topic to learn")
def request_education():
    query("education")


@cli.command(name="rec", help="Ask for a random recreational (active) activity ideas")
def request_recreation():
    query("recreational")


@cli.command(name="social", help="Ask for random social event ideas")
def request_social():
    query("social")


@cli.command(name="diy", help="Ask for random DIY ideas")
def requests_diy():
    query("diy")


@cli.command(name="charity", help="Ask for a random charity idea")
def requests_charity():
    query("charity")


@cli.command(name="cook", help="Ask for random cooking ideas")
def requests_cooking():
    query("cooking")


@cli.command(name="relax", help="Ask for ideas on how to relax ")
def requests_relaxation():
    query("relaxation")


@cli.command(name="music", help="Ask for ideas related to music")
def requests_music():
    query("music")


@cli.command(name="busy_work", help="Ask for ideas related to bsuy work")
def requests_busywork():
    query("busywork")


if __name__ == "__main__":
    print("Thanks for trying this out! -Cam")
    cli()
