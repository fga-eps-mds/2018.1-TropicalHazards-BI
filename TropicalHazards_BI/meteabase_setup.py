import requests
import environ
from settings import BASE_DIR

ENV_DIR = BASE_DIR + '/.env'
env = environ.Env()
env.read_env(ENV_DIR)

METABASE_URL = "http://metabase:3000/api"
FIRST_NAME = env("MB_FIRST_NAME")
LAST_NAME = env("MB_LAST_NAME")
EMAIL = env("MB_EMAIL")
PASSWORD = env("MB_PASSWORD")


def get_setup_token():
    url = METABASE_URL + "/session/properties"
    response = requests.get(url)

    return response.json()["setup_token"]


def initial_setup():
    """ Initial metabase setup, session id is returned"""

    url = METABASE_URL + "/setup"
    token = get_setup_token()

    if not token:
        raise ValueError("No setup token, probably the setup is already done")

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

    response = requests.post(url, json=data)

    return response.json()['id']


def setup_mongo(session_id):
    """ Set mongo as usable db for metabase """
    url = METABASE_URL + '/setup/validate'
    header = "metabase.SESSION_ID={}".format(session_id)

    data = {
        "name": "mongo",
        "engine": "mongo",

        "details": {
            "dbname": "main_db",
            "host": "mongo",
            "port": 27017
        }
    }

    response = requests.post(url, json=data, headers=header)

    if response.status_code == 200:
        return response.json()['id']
    else:
        raise ConnectionError(response.json())
