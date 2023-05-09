import geopandas as gpd
from glob import glob
from sqlalchemy import create_engine
from os.path import basename


def import_to_bd(HOST, USER, PASSWORD, DB_NAME, SCHEMA):
    engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")

    for files in glob(f'{SCHEMA}/*.geojson'):
        name, extension = basename(files).split('.')
        gpd.read_file(files).to_postgis(name=name,
                                        con=engine,
                                        if_exists='append',
                                        schema=SCHEMA)
