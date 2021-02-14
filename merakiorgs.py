import requests
import json
from pprint import pprint

#meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
meraki_api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url =  "https://api.meraki.com/api/v0/"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
org_list =[]
organization =""
orgs = [] # A list containing organisations as JSON
nets = []
org_choice = ""
org_id =""
net_id = "" #Variable holding choice of network id to make subsequent API calls.

# Creates URI for making API call, queries API and processes as json and  prints list of organizations

def list_orgs():
	print("\n","="*8, "Organization List", "="*8)
	path = "organizations"
	url = base_url+path 
	response = requests.request('GET', url=url, headers=headers)
	json_responce = json.loads(response.text)
	n = 0
	for item in json_responce:
		orgs.append(item)
		print("\n", str(n)+".", "ID:", item["id"],"Name:", item["name"])
		n +=1

def choose_org():
	print("Which organization would you like to access?\n")
	org_num = int(input())
	if org_num <= len(orgs)-1:
		org_choice = orgs[org_num]
		org_id = org_choice["id"]
		print()
		print("Accessing the {name} organization.".format(name=org_choice["name"]))
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
		nets.append(item["id"])
		print(str(n)+". ", "ID:", item["id"],"Name:", item["name"], "Time Zone:", item["timeZone"])
		print("    Products:",item["productTypes"])
		n +=1

def choose_net():
	print("hello")
	print("Which network would you like to access?\n")
	net_num = int(input())
	if net_num <= len(nets)-1:
		net_choice = nets[org_num]
		net_id = net_choice["id"]
		print()
		print("Accessing the {name} organization.".format(name=org_choice["name"]))
		list_networks(org_id)
	else:
		print("Invalid entry!!")	

list_orgs()
choose_org()
print(org_id)
#print(orgs)
#print(list_networks(orgs))

#if __name__ == "__main__":
#	list_orgs()
#	org_choose()
	#print("Which organization would you like to access? ")
	#org_choice = int(input())
	#print("Accessing the {org_name} organization.".format(org_name =org_list[org_choice-1]["name"]))
	#(org_name =org_list[org_choice-1]["name"])
