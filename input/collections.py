import const
import requests


resp = requests.get(const.COLLECTION_INDEX_URL)


def get_collection_names(n: int = 200):
    """
    Scrape the names of collections for further processing
    :param n:
    :return:
    """
