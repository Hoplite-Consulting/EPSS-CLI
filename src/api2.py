from src import cveData, utils
import requests

class epss:

    URL = "https://api.first.org/data/v1/epss"

    def __init__(self, verbose: bool = False) -> None:
        self.V = verbose ### Add This later
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
        req = self.session.get(self.URL, params={"cve":cveStr})
        cve = req.json()["data"][0]
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