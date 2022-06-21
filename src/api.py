import requests

class cveData:

    cve = "cve"
    epss = "epss"
    percentile = "percentile"
    date = "date"

    def __init__(self, cve: str = None, epss: float = None, percentile: float = None, date: str = None) -> None:
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

    def __init__(self, verbose: bool = False) -> None:
        self.V = verbose
        self.session = requests.session()

    def _separateList(self, strList: list, separator: str) -> str:
        string = ""
        for i in strList:
            string += i + separator
        return string[:-1]

    def get(self, cveList: str or list) -> cveData or list[cveData]:
        if type(cveList) == list:
            cve = self._separateList(cveList, ",")
        else:
            if cveList == "":
                return cveData(None, None, None, None)
            cve = cveList
        req = self.session.get(self.URL, params={"cve":cve})
        data = req.json()["data"] # Double check this shit
        if self.V:
            print(cve + ": " + str(data))
        if data == []:
            return cveData(None, None, None, None)
        returnList = []
        for response in data:
            returnList.append(cveData(response[cveData.cve], response[cveData.epss], response[cveData.percentile], response[cveData.date]))
        if len(returnList) == 1:
            return returnList[0]
        else:
            return returnList