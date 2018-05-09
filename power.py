#!/usr/bin/env python

import json
import os, time
import requests

# supress Unverified HTTPS request, only do this is a verified environment
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Address of the WTI device
URI = "https://"
SITE_NAME = "192.168.0.158"
BASE_PATH = "/api/v2/config/power"

# put in the username and password to your WTI PDU device here
USERNAME = "super"
PASSWORD = "super"

iCount = 0
iFail  = 0
while (iCount < 10000):
	try:
		print(URI+SITE_NAME+BASE_PATH)
		headersJSON = {'content-type': 'application/json'}
		r = requests.get(URI+SITE_NAME+BASE_PATH, auth=(USERNAME, PASSWORD), verify=False, headers=headersJSON)

		if (r.status_code == 200):
#			os.system('clear')
			parsed_json = r.json()

#			Uncomment to see the JSON return by the unit
#			print parsed_json

			cszStatusCode = parsed_json["status"]["code"][0]
			if (int(cszStatusCode) != 0):
				exit(1)

			if (int(parsed_json['powerunit']) == 0):
				print("NOT a Power Unit. No power Data is avaiable.")
				exit(1)

			if (int(parsed_json['outletmetering']) == 0):
				print("Outlet metering is not available on this unit.")
				exit(1)

			# is the device is an Automaitc Transfer Switch type of power switch
			iATS 		= int(parsed_json['ats'])

			# how many branches (input power plugs)
			iBranchCount 	= int(parsed_json['branchcount'])

			# how many power outlets (output power plugs)
			iPlugCount	= int(parsed_json['plugcount'])

			# how many data power data sets where returned in the JSON
			iDataPoints 	= int(parsed_json['powerdatacount'])

			# how many plugs are assigned to each branch (inpout power plug)
			iPlugsPerBranch = (iPlugCount / iBranchCount);

			iTempDataPoints = 0

			while (iTempDataPoints < iDataPoints):
				iTempBanchCount = 0

				print(BASE_PATH)

				# print the timedate stamp that the follwoing power data was recorded
				print("Data @ "+str(parsed_json['powerdata'][iTempDataPoints]["timestamp"]))

				while (iTempBanchCount < iBranchCount):
					# start reading the Branch block
					print("BRANCH "+str(iTempBanchCount+1)+"")

					cszBranchName = "branch"+str(iTempBanchCount+1)

					# Voltage of the branch being read
					print("    Voltage:         "+parsed_json['powerdata'][iTempDataPoints][cszBranchName][0]['voltage1'] +" (volts)")

					iTempPlugCountCount = 0
					while (iTempPlugCountCount < iPlugsPerBranch):
						# read the current of the plug being read
						cszCurrentName = "current"+str(iTempPlugCountCount+1)

						print("    Plug #"+str(iTempPlugCountCount+1)+" Current: "+parsed_json['powerdata'][iTempDataPoints][cszBranchName][0][cszCurrentName]+"  (amps)")

						# calulate the power (in watts) of the plug being read
						iPower = (float(parsed_json['powerdata'][iTempDataPoints][cszBranchName][0][cszCurrentName]) * float(parsed_json['powerdata'][iTempDataPoints][cszBranchName][0]['voltage1']))
						print("    Plug #"+str(iTempPlugCountCount+1)+" Power:   "+str(iPower)+"  (watts)")

						iTempPlugCountCount = iTempPlugCountCount + 1

					iTempBanchCount = iTempBanchCount + 1

				iTempDataPoints = iTempDataPoints + 1
		else:
			print(r.status_code)

	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print e
		time.sleep(60)
		iFail = iFail + 1
	iCount = iCount + 1
	print("iCount = "+str(iCount)+ ", iFail = "+str(iFail))
	time.sleep(2)
