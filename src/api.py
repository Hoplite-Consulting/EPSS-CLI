from numpy import percentile
import requests

class cveData:

    cve = "cve"
    epss = "epss"
    percentile = "percentile"
    date = "date"

    def __init__(self, cve: str, epss: float, percentile: float, date: str) -> None:
        self.CVE = cve
        self.EPSS = epss
        self.PERCENTILE = percentile
        self.DATE = date

    def __str__(self) -> str:
        return str(self.getDict())

    def getDict(self):
        return {self.cve:self.CVE, self.epss:self.EPSS, self.percentile:self.PERCENTILE, self.date:self.DATE}

class epss:

    URL = "https://api.first.org/data/v1/epss"

    def __init__(self) -> None:
        self.session = requests.session()

    def _separateList(self, strList: list, separator: str) -> str:
        string = ""
        for i in strList:
            string += i + separator
        return string[:-1]

    def get(self, cveList: str or list) -> list[cveData]:
        if type(cveList) == list:
            cve = self._separateList(cveList, ",")
        else:
            cve = cveList
        req = self.session.get(self.URL, params={"cve":cve})
        data = req.json()["data"] # Double check this shit
        returnList = []
        for response in data:
            returnList.append(cveData(response[cveData.cve], response[cveData.epss], response[cveData.percentile], response[cveData.date]))
        return returnList