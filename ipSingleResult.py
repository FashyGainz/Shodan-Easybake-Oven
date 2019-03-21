#
# 03/21/2019
# Author: FashyGainz
# https://github.com/FashyGainz
#
# Most of this code was taken directly from the Shodan dev guide.
# Use this script to look up single host results for whatever you put in api.search()
# This tool should be used in conjunction with the other Shodan scripts in the repo.

import shodan

#insert api key here
SHODAN_API_KEY = "<INSERT YOUR API KEY>"

api = shodan.Shodan(SHODAN_API_KEY)

try:
	results = api.search('blackhat')

	print('Results found: {}'.format(results['total']))
	for result in results['matches']:
		print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
except shodan.APIError, e:
	print('Error: {}'.format(e))

