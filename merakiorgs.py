
import requests
import json
from pprint import pprint

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
base_url =  "https://api.meraki.com/api/v0/"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
org_list =[]
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
	n=1
	
	for item in json_responce:
		org_list.append(item)
		#print(org_list)
		print(str(n)+".", "ID:", item["id"],"Name:", item["name"])
		n=+1
		print()

def org_choose():
	print("Which organization would you like to access? ")
	choice = int(input())
	print("\nAccessing the {org_name} organization.".format(org_name =org_list[choice-1]["name"]))

		

	
if __name__ == "__main__":
	list_orgs()
	org_choose()
	#print("Which organization would you like to access? ")
	#org_choice = int(input())
	#print("Accessing the {org_name} organization.".format(org_name =org_list[org_choice-1]["name"]))
	#(org_name =org_list[org_choice-1]["name"])
