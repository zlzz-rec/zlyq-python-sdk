import sys
sys.path.append('..')

from zlyqsync.private_client import SyncClient
from zlyqmodel.track import TrackCommon, TrackInfo, AppInstall
from zlyqmodel.common import Platform, SdkType, Network, Os, Carrier

if __name__ == "__main__":
    syncClient = SyncClient(projectId=2,
                             apiKey="{your-api-key}",
                             address="{your-track-node}"
                             )

    trackCommon = TrackCommon()
    trackCommon.udid = "abcd"
    trackCommon.user_id = "1234"
    trackCommon.distinct_id = "6039281029182710291"
    trackCommon.platform = Platform.IOS.value
    trackCommon.sdk_type = SdkType.IOS.value
    trackCommon.sdk_version = "1.0.1"
    trackCommon.screen_height = 650
    trackCommon.screen_width = 350
    trackCommon.manufacturer = "huawei"
    trackCommon.model = "huawei P40"
    trackCommon.network = Network.N_4G.value
    trackCommon.os = Os.IOS.value
    trackCommon.os_version = "12.1.1"
    trackCommon.carrier = Carrier.CHINA_UNICOM.value
    trackCommon.app_version = "1.0.1"

    appInstall = AppInstall()
    properties = [appInstall]

    trackInfo = TrackInfo()
    trackInfo.common = trackCommon
    trackInfo.properties = properties
    
    print(syncClient.track(trackInfo))
