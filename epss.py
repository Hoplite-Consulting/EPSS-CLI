#!/usr/bin/python3

from src import *
import os.path as p
from alive_progress import alive_bar
from csv import DictReader
import argparse

def main(args):

    # Set Read / Write Files
    readFile = args.readFile
    if args.writeFile == None:
        writeFile = readFile.split(".")[0]+"_out.csv"
    else:
        writeFile = args.writeFile
    
    # Check if Write File Exists / Ask to overwrite...
    if (p.exists(writeFile)):
            while not args.force:
                rm = input("Do you want to overwrite '" + writeFile + "'? [yes/no]: ")
                if rm.lower() == "no":
                    print("Terminating...")
                    exit()
                elif rm.lower() == "yes":
                    break

    eps = epss_v2(args.verbose)

    # chunkSize = args.chunk ### Option for chunk size from arguments
    chunkSize = 12

    readRows = []
    cveNumbers = []

    # Read from CSV file
    with open(readFile, "r") as read:
        reader = DictReader(read)
        newFields = reader.fieldnames
        newFields.append(cveData.epss)
        newFields.append(cveData.percentile)
        for row in reader:
            readRows.append(row)
    for row in readRows:
        cveNumbers.append(row["CVE"])
    
    # Cleanup Data
    cveNumbers = utils.removeDuplicates(cveNumbers)
    cveNumbers.sort()
    chunks = utils.chunk(cveNumbers, chunkSize)

    cveResponse = []

    # Progress Bar for Loop
    with alive_bar(total=len(cveNumbers), title="Getting EPSS Data...", ctrl_c=False) as bar:
        for chunk in chunks:
            resp = eps.get(chunk)
            for r in resp:
                cveResponse.append(r)
            bar(len(chunk))
    
    utils.writeFile(writeFile, newFields, readRows, cveResponse)

if __name__ == "__main__":

    __version__ = "2.4.1"

    # Args 
    parser = argparse.ArgumentParser(description=f"EPSS CLI Version {__version__}")
    parser.add_argument('readFile', help="Read File Location")
    parser.add_argument('-w', '--writeFile', metavar="", help="Write File Location")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose Output")
    parser.add_argument('-f', '--force', action='store_true', help="Force Overwrite File")
    # parser.add_argument('-c', '--chunk', metavar="12", nargs='?', const=12, type=int, help="Number of CVE's per API request") ### Option for chunk size from arguments
    args = parser.parse_args()

    main(args)
