from dataclasses import dataclass, asdict

import requests
import sys
import json
import os, sys
#lib_path = os.path.abspath(os.path.join('..'))
#sys.path.append(lib_path)

sys.path.append("..")
from auth import sign as signAuth, appToken as appTokenAuth
from model import history, user

@dataclass
class Client():
    appKey:str
    appSecret:str
    appId:int
    address:int

    def __buildHeader(self, params):
        header = {}
        sign, urlParam = signAuth.addSign(params, self.appId, self.appSecret)
        appToken = appTokenAuth.addAppToken(self.appKey, self.appSecret)
        header['Content-Type']: 'application/json'
        header['X-Sign'] = sign
        header['X-App-Token'] = appToken

        return header, urlParam

    def __httpPost(self, address, apiUrl, params, body):
        params = params if params else {}
        header, urlParams = self.__buildHeader(params)
        urlStr = address + apiUrl + "?" + urlParams

        datas = json.dumps(body)
        resp = requests.post(urlStr, data=datas, headers=header)

        return resp.text

    def userInfoSynchronize(self, userInfo):
        body = asdict(userInfo)
        return self.__httpPost(self.address, "/api/v1/synchronize/userInfo", None, body)

    def historySynchronize(self, trackInfo):
        body = asdict(trackInfo)
        return self.__httpPost(self.address, "/trace", None, body)


if __name__ == "__main__":

    '''
    # 同步用户历史交互数据
    trackClient = Client("key", "secret", 123, "http://testtrackapi.zplatform.cn")

    trackCommon = history.TrackCommon()
    trackCommon.udid = "ABC"
    trackCommon.userId = 123 
    trackLike = history.TrackLike()
    trackLike.event = "like"
    trackLike.contentId = 40192918191901
    trackLike.contentType = 1
    trackFinishVideo = history.TrackFinishVideo()
    trackFinishVideo.event = "finishVideo"
    trackFinishVideo.contentId = 40192918191901
    trackFinishVideo.contentType = 1
    trackFinishVideo.videoTime = 15
    trackFinishVideo.duration = 10
    trackFinishVideo.isFinish = 0

    properties = [trackLike, trackFinishVideo]

    trackInfo = history.TrackInfo()
    trackInfo.common = trackCommon
    trackInfo.properties = properties

    print(client.historySynchronize(trackInfo))
    '''


    # 同步用户数据
    userClient = Client("key", "secret", 123, "http://testadminapi.zplatform.cn")

    userInfo = user.UserInfo()
    userInfo.udid = "ABC"
    userInfo.Nickname = "test name"
    userInfo.gender = 1

    print(userClient.userInfoSynchronize(userInfo))
