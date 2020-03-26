### 中量引擎服务端SDK (Python)

##### 安装方法
```
pip install zlyq-python-sdk
```

##### 中量引擎官方文档
```
https://wiki.zplatform.cn/
```

##### SDK说明
本SDK封装了向中量引擎服务同步用户数据、媒资数据及用户历史交互数据的方法

##### 接口调用示例
###### 同步用户历史交互数据
```
    userClient = Client("key", "secret", 123, "http://testappapi.zplatform.cn")

    userInfo = user.UserInfo()
    userInfo.udid = "ABC"
    userInfo.Nickname = "test name"
    userInfo.gender = 1

    print(userClient.userInfoSynchronize(userInfo))
```

###### 同步用户历史交互数据
```
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
```

