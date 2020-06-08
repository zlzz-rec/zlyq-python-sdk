import time
import hashlib

@dataclass
class Signer():
    validTime:int = 5 * 60 * 1000
    apiKey:str = ""

    signature:str = ""
    urlString:str = ""

    def __buildString(self, params):
        if not params:
            return ""
        keys = [key for key in params.keys()]
        keys.sort()

        values = []
        for key in keys:
            values.append(key + '=' + str(params[key]))

        return "&".join(values)

    def __buildSign(self, urlString):
        return hashlib.md5((f"{urlString}&{self.apiKey}").encode(encoding='UTF-8')).hexdigest()

    def genSign(self, urlParams):
        self.urlString = self.__buildString(urlParams)
        self.signature = self.__buildSign(self.urlString)
        return self.signature

    def checkSign(self, sign, urlParams):
        t = int(urlParams.get('time', 0)) if urlParams else 0
        if not t:
            return False
        if int(time.time() * 1000) - t > self.validTime:
            return False

        self.urlString = self.__buildString(urlParams)
        self.signature = self.__buildSign(self.urlString)
        print(f"client sign {sign}")
        print(f"server sign {self.signature}")
        return self.signature.lower() == sign.lower()
