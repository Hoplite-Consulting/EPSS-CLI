#!/bin/python3

from src import *
from alive_progress import alive_it
import argparse

def main(args):
    bar = alive_it(args.cve[0], title="Getting EPSS Data...")
    prev = ""
    for i in bar:
        eps = epss_v2(args.verbose)
        data = eps.get(i.upper())
        try:
            c = data.cve.upper() + ": " + data.CVE
            e = data.epss.upper() + ": " + data.EPSS
            p = data.percentile.capitalize() + ": " + str(float(data.PERCENTILE)*100) + "%"
            d = data.date.capitalize() + ": " + data.DATE
            print(c)
            print(e)
            print(p)
            print(d)
        except TypeError:
            print("No CVE Data Found")
        print("--------------------")

if __name__ == "__main__":

    # Args 
    parser = argparse.ArgumentParser(description="./epss.py <cve>")
    parser.add_argument('cve', action='append', nargs='*', help="CVE Number(s)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose Output")
    args = parser.parse_args()

    main(args)