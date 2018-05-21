import requests
import environ
import os
import time
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = BASE_DIR + '/.env'

env = environ.Env()
env.read_env(ENV_DIR)

METABASE_URL = "http://localhost:3000/api"
FIRST_NAME = env("MB_FIRST_NAME")
LAST_NAME = env("MB_LAST_NAME")
EMAIL = env("MB_EMAIL")
PASSWORD = env("MB_PASSWORD")


def get_setup_token():
    url = METABASE_URL + "/session/properties"
    response = requests.get(url)

    while(response.status_code == 503):
        print("Metabase is still initializing, trying again in 30 seconds")
        time.sleep(30)
        response = requests.get(url)

    return response.json()["setup_token"]


def initial_setup():
    """ Initial metabase setup, session id is returned"""

    url = METABASE_URL + "/setup"
    token = get_setup_token()

    if not token:
        print("Skipping setup, since theres no setup_token")
        sys.exit()

    data = {
        "token": token,
        "user": {
            "first_name": FIRST_NAME,
            "last_name": LAST_NAME,
            "email": EMAIL,
            "password": PASSWORD
        },
        "prefs": {
            "site_name": "Tropical Hazards",
        }
    }
    print("Setting up metabasse superuser")
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Set up of superuser {} finished".format(FIRST_NAME))
    else:
        sys.exit("Setup failed")
    return 0


if __name__ == "__main__":
    print("Waiting metabase start")
    time.sleep(60)

    initial_setup()
