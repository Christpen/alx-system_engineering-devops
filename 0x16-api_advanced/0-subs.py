#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
=======
        """Queries the Reddit API and returns the number of subscribers
            to the subreddit"""
                import requests

                    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                                                        .format(subreddit),
                                                                                    headers={"User-Agent": "My-User-Agent"},
                                                                                                                allow_redirects=False)
                        if sub_info.status_code >= 300:
                                    return 0

                                    return sub_info.json().get("data").get("subscribers")
>>>>>>> 42926ce83ceda471c17de16bcd0c269d7f103840
