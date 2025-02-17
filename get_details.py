import urllib.request
import json

def get_car_details(number: str) -> dict:
    url = f"https://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3&q={number}"
    data = json.load(urllib.request.urlopen(url))
    return data["result"]["records"]