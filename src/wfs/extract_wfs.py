from owslib.wfs import WebFeatureService
from os.path import exists
from os import makedirs
from time import sleep


def extract_data_from_wfs(source_name, wfs_url, bbox):
    wfs = WebFeatureService(wfs_url, version='1.1.0')

    for feature in wfs.contents:
        feature_name = feature.split(':')[1]

        try:
            feature_data = wfs.getfeature(typename=feature, bbox=bbox, outputFormat='application/json')
        except:
            continue

        feature_json = feature_data.getvalue()

        if not exists(f'./{source_name}'):
            makedirs(f'./{source_name}')

        with open(f'./{source_name}/{feature_name}.geojson', 'wb') as f:
            f.write(feature_json)

        sleep(3)
