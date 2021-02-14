
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
orgs = []
org_choice = ""
org_id =""
def list_orgs():
	print("\n","="*8, "Organization List", "="*8)
	path = "organizations"
	url = base_url+path 
	response = requests.request('GET', url=url, headers=headers)
	json_responce = json.loads(response.text)
	n = 0
	for item in json_responce:
		orgs.append(item)
		print("\n", n, "ID:", item["id"],"Name:", item["name"])
		print()
		n +=1

def choose_org():
	print("Choose an organization: ")
	org_num = int(input())
	if org_num <= len(orgs)-1:
		org_choice = orgs[org_num]
		org_id = org_choice["id"]
		print()
		print("You chose the {name} organization.".format(name=org_choice["name"]))
		list_networks(org_id)
	else:
		print("Invalid entry!!")
	
		
def list_networks(org_choice):
	print("\n","="*8, "Network List","="*8)
	path = "organizations/"+org_choice+"/networks"
	url = base_url+path
	print(url)
	response = requests.request('GET', url=url, headers=headers)
	json_responce = json.loads(response.text)
	n = 0
	for item in json_responce:
		orgs.append(item["id"])
		print("\n", n, "ID:", item["id"],"Name:", item["name"], "Time Zone:", item["timeZone"])
		print("Products:",item["productTypes"])
		print()
		n +=1

	

list_orgs()
choose_org()
print(org_id)
#print(orgs)
#print(list_networks(orgs))
