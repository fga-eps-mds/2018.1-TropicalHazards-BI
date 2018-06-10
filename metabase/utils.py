import requests
import json

from TropicalHazards_BI import settings
from metabase.models import MetabaseSession

MB_USERNAME = settings.env("MB_EMAIL")
MB_PASSWORD = settings.env("MB_PASSWORD")

MB_URL = 'http://metabase:3000/api'


def login_metabase():
    url = MB_URL + '/session'
    print(MB_USERNAME + MB_PASSWORD)
    data = {'username': MB_USERNAME, 'password': MB_PASSWORD}
    session = MetabaseSession.objects.first()

    if session:
        session_id = session.session_id
    else:
        login = requests.post(url, json=data)
        if login.status_code == 200:
            session = MetabaseSession.objects.\
                        create(session_id=login.json()['id'])
            session_id = session.session_id
        else:
            raise Exception('Cannot login on metabase - ' + login.json())

    return session_id



def get_database_id(database_name: str):
    url = MB_URL + '/database'
    session_id = login_metabase()
    header = {'Cookie': 'metabase.SESSION_ID=' + session_id}

    databases = requests.get(url, headers=header)

    for database in databases.json():
        if database['name'] == database_name:
            return database['id']

    return None


def get_table_id(database_id, table_name):
    url = MB_URL + '/database'
    params = {'include_tables': 'true'}

    session_id = login_metabase()
    header = {'Cookie': 'metabase.SESSION_ID=' + session_id}

    databases = requests.get(url, headers=header, params=params)

    for database in databases.json():
        if database['id'] == database_id:
            for table in database['tables']:
                if table['name'] == table_name:
                    return table['id']

    return None
