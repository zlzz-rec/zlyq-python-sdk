from dataclasses import dataclass, asdict
from requests_toolbelt.multipart.encoder import MultipartEncoder

import sys
sys.path.append("..")
from zlyqauth import private_sign as signAuth

import requests
import json

@dataclass
class SyncClient():
    projectId:int
    apiKey:str
    address:str

    def __buildHeader(self, params):
        header = {}
        sign, urlParam = signAuth.addSign(params, self.apiKey)
        header['Content-Type'] = 'application/json'
        header['X-Sign'] = sign

        return header, urlParam

    def __httpPost(self, address, apiUrl, params, body):
        params = params if params else {}
        header, urlParams = self.__buildHeader(params)
        urlStr = address + apiUrl + "?" + urlParams

        datas = json.dumps(body)
        resp = requests.post(urlStr, data=datas, headers=header)

        return resp.text

    def __httpMultiForm(self, address, apiUrl, params, body):
        params = params if params else {}
        header, urlParams = self.__buildHeader(params)
        urlStr = address + apiUrl + "?" + urlParams

        multipart_encoder = MultipartEncoder(
            fields=body,
        )
        header['Content-Type'] = multipart_encoder.content_type
        resp = requests.post(
            urlStr,
            data=multipart_encoder,
            headers=header)

        return resp.text

    def track(self, trackInfo):
        body = asdict(trackInfo)
        return self.__httpPost(self.address, "/test_trace", None, body)

    def setUserProfile(self, userProfile):
        body = asdict(userProfile)
        return self.__httpPost(self.address, f"/api/v1/profile/{self.projectId}/user", None, body)
