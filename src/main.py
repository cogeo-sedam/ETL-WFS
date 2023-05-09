from os import environ
from wfs import extract_data_from_wfs
from postgis import import_to_bd

if __name__ == '__main__':
    EXTERNAL_SOURCE_URL = environ['EXTERNAL_SOURCE_URL']

    DB_HOST = environ['DB_HOST']
    DB_USER = environ['DB_USER']
    DB_PASSWORD = environ['DB_PASSWORD']
    DB_NAME = environ['DB_NAME']
    DB_SCHEMA = environ['DB_SCHEMA']

    RONDONIA_BBOX = (-66.8102531119998986, -13.6937001229999389, -59.7743574309999204, -7.9758682970000194)

    extract_data_from_wfs(DB_SCHEMA, EXTERNAL_SOURCE_URL, RONDONIA_BBOX)
    import_to_bd(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_SCHEMA)
