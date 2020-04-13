import sys

sys.path.append('..')

from zlyqsync.client import SyncClient
from zlyqmodel.video import *
import time

def syncVideo():
    videoClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    videos = VideoSyncInfos()

    v = VideoSyncInfo(title="title test",
                      userId="457751121931763712",
                      content="content test",
                      uploadType=0,
                      orgFileName="video.mp4",
                      os=1,
                      deviceId="wdfvrehr234",
                      ip="",
                      longitude=30,
                      latitude=120,
                      audioId=0,
                      source=1,
                      thirdId="fenwkl",
                      thirdExtra="",
                      createdAt=int(time.time() * 1000))

    videos.add(v)

    print(videoClient.videoSynchronize(videos))

def uploadVideo():
    videoClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    vf = open("test.mp4", "rb")
    img = open("test.jpg", "rb")

    v = VideoUploadInfo(video=vf.read(),
                        image=img.read(),
                        title="title test",
                        userId="457751121931763712",
                        content="content test",
                        orgFileName="test.mp4",
                        os=1,
                        source=1,
                        thirdId="fenwkl",
                        thirdExtra="",)

    print(videoClient.videoUpload(v))


if __name__ == "__main__":
    syncVideo()
    # uploadVideo()
