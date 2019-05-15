#!/usr/bin/env python

import json
import requests

# supress Unverified HTTPS request, only do this is a verified environment
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Address of the WTI device
URI = "https://"
SITE_NAME = "rest.wti.com"
BASE_PATH = "/api/v2/config/power"

# put in the username and password to your WTI PDU device here
USERNAME = "restpowerpublic"
PASSWORD = "restfulpassword"

print("\n\nWTI Plug Power request program")
print("----------------------------\n")

tempdata = input("Enter URI [default: %s ]: " % (URI))
if (len(tempdata) > 0):
	URI = tempdata

tempdata = input("Enter SITE_NAME [default: %s ]: " % (SITE_NAME))
if (len(tempdata) > 0):
    SITE_NAME = tempdata

tempdata = input("Enter USERNAME [default: %s ]: " % (USERNAME))
if (len(tempdata) > 0):
    USERNAME = tempdata

tempdata = input("Enter PASSWORD [default: %s ]: " % (PASSWORD))
if (len(tempdata) > 0):
    PASSWORD = tempdata

try:
    print("%s%s%s" % (URI, SITE_NAME, BASE_PATH))
    headersJSON = {'content-type': 'application/json'}
    r = requests.get(URI+SITE_NAME+BASE_PATH, auth=(USERNAME, PASSWORD), verify=False, headers=headersJSON)
    if (r.status_code == 200):
        parsed_json = r.json()
        print(parsed_json)

        statuscode = parsed_json["status"]["code"][0]
        if (int(statuscode) != 0):
            exit(1)

        if (int(parsed_json['powerunit']) == 0):
            print("NOT a Power Unit. No power Data is avaiable.")
            exit(1)

        if (int(parsed_json['outletmetering']) == 0):
            print("Outlet metering is not available on this unit.")
            exit(1)

        # is the device is an Automaitc Transfer Switch type of power switch
        ats = int(parsed_json['ats'])

        # how many branches (input power plugs)
        branchcount = int(parsed_json['branchcount'])

        # how many power outlets (output power plugs)
        plugcount = int(parsed_json['plugcount'])

        # how many data power data sets where returned in the JSON
        datapoints = int(parsed_json['powerdatacount'])

        # how many plugs are assigned to each branch (inpout power plug)
        plugsperbranch = (plugcount / branchcount)

        tempdatapoints = 0

        while (tempdatapoints < datapoints):
            tempbranchcount = 0

            print(BASE_PATH)

            # print the timedate stamp that the follwoing power data was recorded
            print("Data @ %s" % (parsed_json['powerdata'][tempdatapoints]["timestamp"]))

            while (tempbranchcount < branchcount):
                # start reading the Branch block
                print("BRANCH %d" % (tempbranchcount+1))

                branchname = ("branch%d" % (tempbranchcount+1))

                # Voltage of the branch being read
                print("    Voltage:         %s (volts)" % (parsed_json['powerdata'][tempdatapoints][branchname][0]['voltage1']))

                tempplugcount = 0
                while (tempplugcount < plugsperbranch):
                    # read the current of the plug being read
                    currentname = ("current%d" % (tempplugcount+1))

                    print("    Plug #%d Current: %s  (amps)" % (tempplugcount+1, parsed_json['powerdata'][tempdatapoints][branchname][0][currentname]))

                    # calulate the power (in watts) of the plug being read
                    iPower = (float(parsed_json['powerdata'][tempdatapoints][branchname][0][currentname]) * float(parsed_json['powerdata'][tempdatapoints][branchname][0]['voltage1']))
                    print("    Plug #%d Power:   %.1f  (watts)" % (tempplugcount+1, iPower))

                    tempplugcount += 1

                tempbranchcount += 1

            tempdatapoints += 1
    else:
        print(r.status_code)
        print(r.reason)

except requests.exceptions.RequestException as e:  # This is the correct syntax
    print (e)
