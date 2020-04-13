from zlyqsync.client import SyncClient
from zlyqmodel.image import *
import time
import sys

sys.path.append('..')


def uploadImage():
    imageClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    # 请按需求调整test.jpg
    with open("test.jpg", "rb") as f:
        x = f.read()

        i = Image(userId="457751121931763712",
                  image=x,
                  description="image description",
                  source=1,
                  thirdId="fdanklh",
                  thirdExtra="")

        print(imageClient.imageUpload(i))


if __name__ == "__main__":
    uploadImage()
