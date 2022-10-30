from turtle import done
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


    def requests_bored_api_recreation(subject):
        """Query the bored API to find something to do.  You 
        can change which argument you pass through this method with any of the strings in
        the activities list.  Choose an activity you feel like trying something new in."""

        hit_api = requests.get("http://www.boredapi.com/api/activity?type=" + subject)
        hit_api.encoding = "utf-8"
        hit_api.text
        find_key = hit_api.json()
        print(f"{subject.capitalize()} event: {find_key['activity']}")

    def suggestion_for_each_activity():
        for all in activities:
            APIs.requests_bored_api_recreation(all)
            
    def request_recreation():
        APIs.requests_bored_api_recreation("recreational")

    def request_social():
        APIs.requests_bored_api_recreation("social")

    def requests_diy():
        APIs.requests_bored_api_recreation("diy")

    def requests_charity()





suggestion_for_each_activity()   
#request_for_recreation()


# activity.iterate_through_activities()
