import sys
sys.path.append('..')

from zlyqsync.client import SyncClient
from zlyqmodel.history import TrackInfo, TrackCommon, TrackLike, TrackFinishVideo

if __name__ == "__main__":
    trackClient = SyncClient("{your-app-key}", "{your-app-secret}", 123, "http://testtrackapi.zplatform.cn")

    trackCommon = TrackCommon()
    trackCommon.udid = "ABC"
    trackCommon.userId = 123
    trackLike = TrackLike()
    trackLike.event = "like"
    trackLike.contentId = 40192918191901
    trackLike.contentType = 1
    trackFinishVideo = TrackFinishVideo()
    trackFinishVideo.event = "finishVideo"
    trackFinishVideo.contentId = 40192918191901
    trackFinishVideo.contentType = 1
    trackFinishVideo.videoTime = 15
    trackFinishVideo.duration = 10
    trackFinishVideo.isFinish = 0
    
    properties = [trackLike, trackFinishVideo]
    
    trackInfo = TrackInfo()
    trackInfo.common = trackCommon
    trackInfo.properties = properties
    
    print(trackClient.historySynchronize(trackInfo))
