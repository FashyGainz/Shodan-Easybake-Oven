#
# 03/21/2019
# Author: FashyGainz
# https://github.com/FashyGainz
#
# Most of this code was taken directly from the Shodan dev guide.
# Use this script to look up available information from ip addresses in a list, then output the results to stdout in a cleaner format.
# This tool should be used in conjunction with the other Shodan scripts in the repo.

import json
import shodan
import argparse
import time
SHODAN_API_KEY = "<INSERT YOUR API KEY>"
api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Get a list of IPs and return shodan info.')
parser.add_argument('--filename', '-f', default='iplist.txt')
args=parser.parse_args()

with open(args.filename, 'r') as f:
        ips = [line.strip() for line in f]

awsInfo = {}
for ip in ips:
        try:
                print "Retrieving Info"
                hostinfo = api.host(ip)
                awsInfo[ip] = hostinfo
                time.sleep(2)
                print "Info collected, dumping raw output for host"

		#new clean print job 
		print hostinfo

        except shodan.APIError, e:
                awsInfo[ip] = '{}'.format(e)
                time.sleep(2)
                print "No information found, giving up on host"

# Old dirty print job
#print json.dumps(awsInfo)
