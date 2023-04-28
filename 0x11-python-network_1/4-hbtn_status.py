#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    content = response.text
    content_type = type(content)

    print("Body response:")
    print("\t- type: {}".format(content_type))
    print("\t- content: {}".format(content))

