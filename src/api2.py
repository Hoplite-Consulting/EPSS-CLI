from src import cveData, utils
import requests

class epss:

    URL = "https://api.first.org/data/v1/epss"

    def __init__(self, verbose: bool = False, date: str = None) -> None:
        self.V = verbose
        self.DATE = date
        self.session = requests.session()

    def _list(self, cveList: list) -> list[cveData]:
        returnList = []
        if self.V:
            print("API Requesting: " + str(cveList))
        req = self.session.get(self.URL, params={"cve":utils.splitStrList(cveList, ",")})
        data = req.json()["data"]
        for cve in data:
            returnList.append(cveData(cve[cveData.cve], cve[cveData.epss], cve[cveData.percentile], cve[cveData.date]))
        return returnList

    def _str(self, cveStr: str) -> cveData:
        if self.V:
            print("API Requesting: " + str(cveStr))
        if self.DATE:
            req = self.session.get(self.URL, params={"cve":cveStr, "date":self.DATE})
        else:
            req = self.session.get(self.URL, params={"cve":cveStr})
        data = req.json()["data"]
        if req.json()["status-code"] != 200:
            return cveData()
        else:
            try:
                cve = data[0]
            except IndexError:
                return cveData()
            return cveData(cve[cveData.cve], cve[cveData.epss], cve[cveData.percentile], cve[cveData.date])

    def get(self, cveList: str | list) -> cveData | list[cveData]:
        try:
            if len(cveList) > 0:
                if type(cveList) == str and len(cveList) > 3:
                    return self._str(cveList)
                elif type(cveList) == list and len(cveList) > 0:
                    return self._list(cveList)
            else:
                return cveData()
        except TypeError as e:
            raise TypeError("Variable 'cveList' must be a string or a list.") from e