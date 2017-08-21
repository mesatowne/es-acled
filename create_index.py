import requests
import os

from requests.auth import HTTPBasicAuth

ES_HOST = os.environ.get("ES_HOST")
ES_USER = os.environ.get("ES_USER")
ES_PASSWORD = os.environ.get("ES_PASSWORD")
ES_ACLED_INDEX = os.environ.get("ES_ACLED_INDEX")
URL = ES_HOST + ES_ACLED_INDEX

def create_indice(delete=None):

    if delete:
        requests.delete(URL, auth=HTTPBasicAuth(ES_USER, ES_PASSWORD))

    template = open("elasticsearch/acled-template.json").read()
    res = requests.put(URL, data=template, auth=HTTPBasicAuth(ES_USER, ES_PASSWORD))

    print res.content


if __name__ == "__main__":
    delete = raw_input("Want to delete the actual '{0}' index? Y/N: ".format(ES_ACLED_INDEX)) == "Y"
    create_indice(delete)