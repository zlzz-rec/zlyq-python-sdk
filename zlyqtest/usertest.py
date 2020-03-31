import sys
sys.path.append('..')

from zlyqsync.client import SyncClient
from zlyqmodel.user import UserInfo

if __name__ == "__main__":
    userClient = SyncClient(
            appKey = "29d9c1ec0eeaaa4eed534d676633a909", 
            appSecret = "c3bf54192a63f047030f0bfb83df6055", 
            appId = 457639568360448000,
            address = "http://testappapi.zplatform.cn"
    )
    
    userInfo = UserInfo()
    userInfo.thirdId = '51982'
    userInfo.udid = "ABC"
    userInfo.nickname = "test name"
    userInfo.gender = 1
    userInfo.account = "xiaoming"
    userInfo.avatar = "http://www.baidu.com"
    userInfo.phone = "10000000000"

    print(userClient.userInfoSynchronize(userInfo))
