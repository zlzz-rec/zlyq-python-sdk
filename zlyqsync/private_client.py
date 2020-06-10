from dataclasses import dataclass, asdict
from requests_toolbelt.multipart.encoder import MultipartEncoder
from ..zlyqauth.private_sign import Signer
from ..zlyqmodel.common_define import DebugMode

import requests
import json
import time

@dataclass
class SyncClient():
    project_id:int
    api_key:str
    address:str
    debug_mode:str = DebugMode.NO_DEBUG_MODE.value

    def __buildHeader(self, params):
        header = {}
        signer = Signer(apiKey=self.api_key)
        sign = signer.genSign(params)
        header['Content-Type'] = 'application/json'
        header['Z-Sign'] = sign

        return header, signer.urlString

    def __httpPost(self, address, apiUrl, params, body):
        params = params if params else {}
        params['time'] = int(time.time() * 1000)
        header, urlParams = self.__buildHeader(params)
        urlStr = address + apiUrl + "?" + urlParams
        datas = json.dumps(body)
        resp = requests.post(urlStr, data=datas, headers=header)

        return resp.text

    def track(self, trackInfo):
        trackInfo.project_id = self.project_id
        trackInfo.debug_mode = self.debug_mode
        body = asdict(trackInfo)
        return self.__httpPost(self.address, f"/api/v1/track/{self.project_id}", None, body)

    def setUserProfile(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "set"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def setUserProfileOnce(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "set_once"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def appendUserProfile(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "append"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def increaseUserProfile(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "increase"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def deleteUserProfile(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "delete"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def unsetUserProfile(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "unset"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

if __name__ == "__main__":
    syncClient = SyncClient(project_id=1,
                    api_key="{your-api-key}",
                    address="{your-address}"
                    )

