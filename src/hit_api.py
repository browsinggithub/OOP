import requests

class Bored:
    def __init__(self, url):
        self.url = url


    activities = {
        "education",
        "recreational",
        "social",
        "diy",
        "charity",
        "cooking",
        "relaxation",
        "music",
        "busywork",
    }

    def requests_bored_api_activity(self, activity):
        """Query the bored API to find something to do.  You 
        can change which argument you pass through this method with any of the strings in
        the activities list.  Choose an activity you feel like trying something new in."""

        hit_api = requests.get(self.url + activity)
        hit_api.encoding = "utf-8"
        hit_api.text
        find_key = hit_api.json()
        print(f"{activity.capitalize()} event: {find_key['activity']}")
        return 

    def suggestion_for_each_activity(self, all):
        """get a suggestion of something to do for any activity"""
        hit_api = requests.get(self.url + activity)
        hit_api.encoding = "utf-8"
        hit_api.text
        find_key = hit_api.json()
        for all in activity:
            print(f"{all.capitalize()} Event: {find_key['activity']}")

        

activity = Bored("http://www.boredapi.com/api/activity?type=")

activity.requests_bored_api_activity("education")


# activity.iterate_through_activities()
