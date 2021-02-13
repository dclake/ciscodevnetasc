
import requests
import json
from pprint import pprint

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
base_url =  "https://api.meraki.com/api/v0/"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
# Creates URI for making API call, 
# queries API and processes as json
# Finally prints list of organizations
def list_orgs():
	print("\n","="*8, "Organization List", "="*8)
	path = "organizations"
	url = base_url+path 
	#return url 
	response = requests.request('GET', url=url, headers=headers)
	json_responce = json.loads(response.text)
	for item in json_responce:
		print("ID:", item["id"])
		print("Name:", item["name"])
		print()

		
		

	

list_orgs()
