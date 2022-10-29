import requests

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
class api:
    def __init__(self, url):
        self.url = url

    def requests_bored_api_activity(self, activity):

        hit_api = requests.get(self.url + activity)
        hit_api.encoding = "utf-8"
        hit_api.text
        find_key = hit_api.json()
        print(f"{activity.capitalize()} event: {find_key['activity']}")

        


activity = api("http://www.boredapi.com/api/activity?type=")

activity.requests_bored_api_activity("recreational")

# activity.iterate_through_activities()
