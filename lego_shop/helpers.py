import decimal
import requests
import requests_cache
import json


requests_cache.install_cache('image_cache', backend='sqlite')

def gimme_legos(search):
    url = f"https://rebrickable.com/api/v3/lego/sets/?search={search}"

    

    headers = {
        "Accept": 'application/json',
        "Authorization": "key b70e725635e56d4a60589c70b98a8bae",
        
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# def get_image(search):
#     url = "https://google-search72.p.rapidapi.com/imagesearch"

#     querystring = {"q":"search","gl":"us","lr":"lang_en","num":"10","start":"0"}

#     headers = {
#         "X-RapidAPI-Key": "0e9e06a6bdmsh4fb4095b0bc08c5p1bdd16jsnb4eac2ec2419",
#         "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     data = response.json()

#     img_url = ""

#     if 'items' in data.keys():
#         img_url = data['items'][0]['originalImageUrl']#data object, index for the path

#     print(img_url)
#     return img_url

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj)