#!/bin/python3

from src import *
from alive_progress import alive_bar
import argparse

def main(args):
    for i in args.cve[0]:
        with alive_bar(title="Getting EPSS Data...") as bar:
            eps = epss_v2(args.verbose)
            data = eps.get(i.upper())
            bar()
        try:
            print(data.cve.upper() + ": " + data.CVE)
            print(data.epss.upper() + ": " + data.EPSS)
            print(data.percentile.capitalize() + ": " + str(float(data.PERCENTILE)*100) + "%")
            print(data.date.capitalize() + ": " + data.DATE)
        except TypeError:
            print("No CVE Data Found")

if __name__ == "__main__":

    # Args 
    parser = argparse.ArgumentParser(description="./epss.py <cve>")
    parser.add_argument('cve', action='append', nargs='*', help="CVE Number(s)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose Output")
    args = parser.parse_args()

    main(args)