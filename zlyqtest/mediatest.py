from ..zlyqsync.client import SyncClient
from ..zlyqmodel.media import *
import time


def syncMediaLike():
    mediaClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    mls = MediaLikes()

    m = MediaLike(mediaId="467366407865606144",
                  userId="457751121931763712",
                  createdAt=int(time.time() * 1000))

    mls.add(m)

    print(mediaClient.mediaLikeSynchronize(mls))


def syncMediaFavorite():
    mediaClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    mfs = MediaFavorites()

    m = MediaFavorite(mediaId="467366407865606144",
                      userId="457751121931763712",
                      createdAt=int(time.time() * 1000))

    mfs.add(m)

    print(mediaClient.mediaFavoriteSynchronize(mfs))


def syncComment():
    mediaClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    comments = Comments()

    c = Comment(mediaId="467366407865606144",
                userId="457751121931763712",
                content="comment content",
                thirdId="cdew",
                createdAt=int(time.time() * 1000))

    comments.add(c)

    print(mediaClient.commentSynchronize(comments))


def syncCommentLike():
    mediaClient = SyncClient(
        appKey="bb4ddb451bdd80af204d9f464fbf07df",
        appSecret="2d4964bbafde4bf415f9e5b81c4556b3",
        appId=450007472627785728,
        address="http://testappapi.zplatform.cn"
    )

    cls = CommentLikes()

    c = CommentLike(mediaId="467366407865606144",
                    userId="457751121931763712",
                    commentId="467428084384505856",
                    createdAt=int(time.time() * 1000))

    cls.add(c)

    print(mediaClient.commentLikeSynchronize(cls))


if __name__ == "__main__":
    syncMediaLike()
    syncMediaFavorite()
    syncComment()
    syncCommentLike()
