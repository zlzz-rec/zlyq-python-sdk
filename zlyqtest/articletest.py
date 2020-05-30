import time

from ..zlyqmodel.article import *
from ..zlyqsync.client import SyncClient

def syncArticle():
    articleClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    articles = ArticleSyncInfos()

    a = ArticleSyncInfo(title="title test",
                        userId="457751121931763712",
                        content="content test",
                        h5content="",
                        os=1,
                        deviceId="dewc",
                        ip="",
                        longitude=30,
                        latitude=120,
                        source=1,
                        mediaType=2,
                        thirdId="fdanklh",
                        thirdExtra="",
                        createdAt=int(time.time() * 1000))

    articles.add(a)

    print(articleClient.articleSynchronize(articles))


def uploadArticle():
    articleClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    a = ArticleUploadInfo(coverIds=[],
                          galleryIds=["455522923617492992"],
                          title="title test",
                          userId="457751121931763712",
                          content="content test",
                          h5content="",
                          os=1,
                          source=1,
                          mediaType=2,
                          thirdId="fdanklh",
                          thirdExtra="")

    print(articleClient.articleUpload(a))


if __name__ == "__main__":
    # syncArticle()
    uploadArticle()
