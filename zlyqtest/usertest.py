import sys
sys.path.append('..')

from zlyqsync.client import SyncClient
from zlyqmodel.user import UserInfo

if __name__ == "__main__":
    userClient = SyncClient("key", "secret", 123, "http://testappapi.zplatform.cn")
    userInfo = UserInfo()
    userInfo.udid = "ABC"
    userInfo.Nickname = "test name"
    userInfo.gender = 1
    print(userClient.userInfoSynchronize(userInfo))
