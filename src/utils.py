from csv import DictWriter
from src import cveData
from alive_progress import alive_bar

def chunk(li: list, size: int) -> list[list]:
    return list(li[pos:pos + size] for pos in range(0, len(li), size))

def removeDuplicates(li: list) -> list:
    return list(filter(None, list(dict.fromkeys(li))))

def splitStrList(strList: list, separator: str) -> str:
    string = ""
    for i in strList:
        string += i + separator
    return string[:-1]

def writeFile(path: str, fields: list, originalData: list[dict], newData: list[cveData]) -> None:
    with open(path, "w") as file, alive_bar(total=len(originalData), title="Saving EPSS Data...", ctrl_c=False) as bar:
        writer = DictWriter(file, fields)
        writer.writeheader()
        for row in originalData:
            cve = row["CVE"]
            for new in newData:
                # print(cve + " " + new.CVE)
                # print(cve == new.CVE)
                # print("\n")
                if new.CVE == cve:
                    row[cveData.epss] = new.EPSS
                    row[cveData.percentile] = new.PERCENTILE
                    break
            bar()
            writer.writerow(row)