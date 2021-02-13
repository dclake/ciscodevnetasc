
import requests
import json
from pprint import pprint

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
url =  "https://api.meraki.com/api/v0/organizations"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
#orgs = requests.get(url,headers=headers)
#print(orgs)
#print(json.dumps(orgs.json(), indent=4))

response = requests.request('GET', url=url, headers=headers)
json_responce = json.loads(response.text)
# print(response.text)
print()
print("="*5,"Lisiting Organizations","="*5)
for item in json_responce:
	print("ID:",item["id"])
	print("Name:",item["name"])
