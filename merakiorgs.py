
import requests
import json
from pprint import pprint

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
base_url =  "https://api.meraki.com/api/v0/"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
org_list =[]
organization =""
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
<<<<<<< HEAD
	n=1
	
	for item in json_responce:
		org_list.append(item)
		#print(org_list)
		print(str(n)+".", "ID:", item["id"],"Name:", item["name"])
		n=+1
=======
	n = 0
	for item in json_responce:
		orgs.append(item)
		print("\n", n, "ID:", item["id"],"Name:", item["name"])
>>>>>>> 2bcd9d213851c6267146f9cf4274ed2b0553a4b2
		print()
		n +=1

<<<<<<< HEAD
def org_choose():
	print("Which organization would you like to access? ")
	choice = int(input())
	organization = org_list[choice-1]["id"]
	print("\nAccessing the {org_name} organization.".format(org_name =org_list[choice-1]["name"]))
	print(organization)

		

	
if __name__ == "__main__":
	list_orgs()
	org_choose()
	#print("Which organization would you like to access? ")
	#org_choice = int(input())
	#print("Accessing the {org_name} organization.".format(org_name =org_list[org_choice-1]["name"]))
	#(org_name =org_list[org_choice-1]["name"])
=======
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
>>>>>>> 2bcd9d213851c6267146f9cf4274ed2b0553a4b2
