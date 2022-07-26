#!/usr/bin/python3

from src import *
from alive_progress import alive_it
import argparse
import os.path as p

def main(args):
    bar = alive_it(args.cve[0], title="Getting EPSS Data...")
    for i in bar:
        if args.date and utils.checkDate(args.date):
            eps = epss_v2(args.verbose, args.date)
        else:
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
            if args.writeFile:
                with open(args.writeFile, "a") as f:
                    f.writelines([c+"\n", e+"\n", p+"\n", d+"\n", "--------------------\n"])
        except TypeError:
            print("No CVE Data Found")
            if args.writeFile:
                with open(args.writeFile, "a") as f:
                    f.writelines(["No CVE Data Found\n", "--------------------\n"])
        print("--------------------")

if __name__ == "__main__":

    __version__ = "2.4.1"

    # Args 
    parser = argparse.ArgumentParser(description=f"CVE EPSS CLI Version {__version__}")
    parser.add_argument('cve', action='append', nargs='*', help="CVE Number(s)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose Output")
    parser.add_argument('-w', '--writeFile', metavar="path" ,nargs="?", type=str, help="Path to Output File")
    parser.add_argument('-f', '--force', action='store_true', help="Force Overwirte File")
    parser.add_argument('-d', '--date', metavar="yyyy-mm-dd", help="Date for CVE lookup")
    args = parser.parse_args()

    if args.writeFile:
        if (p.exists(args.writeFile)):
                while not args.force:
                    rm = input("Do you want to overwrite '" + args.writeFile + "'? [yes/no]: ")
                    if rm.lower() == "no":
                        print("Terminating...")
                        exit()
                    elif rm.lower() == "yes":
                        break
        with open(args.writeFile, "w") as f:
            f.close()

    main(args)
