#
# 03/20/2019
# Author: FashyGainz
# https://github.com/FashyGainz
#
# Most of this code was taken directly from the Shodan dev guide.
# Use this script to parse ip addresses in a file and filters by tags listed in the array below. It then makes the results readable and digestible.
# This tool should be used in conjunction with the other Shodan scripts in the repo.


# Import the method that helps us parse the data file
from shodan.helpers import iterate_files, open_file, write_banner

# Standard Python libraries
from pprint import pprint
from sys import argv, exit

# Settings
OUTPUT_FILENAME = 'iterate-query.json.gz'

# The user has to provide at least 1 file
if len(argv) == 1:
    print('Usage: {} <file1.json.gz> [file2.json.gz] ...'.format(argv[0]))
    exit(1)

# Create the output file
with open_file(OUTPUT_FILENAME) as fout:
    # Iterate over all of the provided data files
    for banner in iterate_files(argv[1:]):
        # Is the service listed?
        if 'tags' in banner and 'vpn' or 'http' or 'https' or 'ftp' or 'telnet' or 'smtp' or 'ssh' or 'mysql' or 'mssql' or 'snmp' in banner['tags']:
            # Show the banner
            pprint(banner)

            # Store it in the output file
            write_banner(fout, banner)
