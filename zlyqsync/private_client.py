from dataclasses import dataclass, asdict
from requests_toolbelt.multipart.encoder import MultipartEncoder
from ..zlyqauth import private_sign as signAuth
from ..zlyqmodel.common_define import DebugMode

import requests
import json

@dataclass
class SyncClient():
    project_id:int
    api_key:str
    address:str
    debug_mode:str = DebugMode.NO_DEBUG_MODE.value

    def __buildHeader(self, params):
        header = {}
        sign, urlParam = signAuth.addSign(params, self.api_key)
        header['Content-Type'] = 'application/json'
        header['X-Sign'] = sign

        return header, urlParam

    def __httpPost(self, address, apiUrl, params, body):
        params = params if params else {}
        header, urlParams = self.__buildHeader(body)
        urlStr = address + apiUrl + "?" + urlParams

        datas = json.dumps(body)
        resp = requests.post(urlStr, data=datas, headers=header)

        return resp.text

    def __httpMultiForm(self, address, apiUrl, params, body):
        params = params if params else {}
        header, urlParams = self.__buildHeader(body)
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

    def appendUserProfileOnce(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "append"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def increaseUserProfileOnce(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "increase"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def deleteUserProfileOnce(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "delete"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

    def unsetUserProfileOnce(self, userProfileInfo):
        userProfileInfo.project_id = self.project_id
        userProfileInfo.debug_mode = self.debug_mode
        userProfileInfo.common.type = "unset"
        body = asdict(userProfileInfo)
        return self.__httpPost(self.address, f"/api/v1/user_profile/{self.project_id}", None, body)

if __name__ == "__main__":
    syncClient = SyncClient(project_id=2,
                    api_key="{your-api-key}",
                    address="{your-address}"
                    )

