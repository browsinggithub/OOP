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

class APIs:
    def __init__(self, url):
        self.url = url


    

    def requests_bored_api_activity(self, subject):
        """Query the bored API to find something to do.  You 
        can change which argument you pass through this method with any of the strings in
        the activities list.  Choose an activity you feel like trying something new in."""

        hit_api = requests.get(self.url + subject)
        hit_api.encoding = "utf-8"
        hit_api.text
        find_key = hit_api.json()
        print(f"{subject.capitalize()} event: {find_key['activity']}")
        return 

    def suggestion_for_each_activity(self):
        """get a suggestion of something to do for any activity"""
        for all in activities:
            hit_api = requests.get(self.url + all)
            hit_api.encoding = "utf-8"
            hit_api.text
            find_key = hit_api.json()
            print(f"{all.capitalize()} Event: {find_key['activity']}")

        

activity = APIs("http://www.boredapi.com/api/activity?type=")

activity.requests_bored_api_activity("education")
activity.suggestion_for_each_activity()


# activity.iterate_through_activities()
