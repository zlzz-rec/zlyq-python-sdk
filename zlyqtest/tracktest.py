from ..zlyqsync.private_client import SyncClient
from ..zlyqmodel.track import TrackCommon, TrackInfo, AppInstall
from ..zlyqmodel.common_define import Platform, SdkType, Network, Os, Carrier

if __name__ == "__main__":
    sync_client = SyncClient(project_id=2,
                            #api_key="{your-api-key}",
                            #address="{your-address}",
                            api_key="abcdefg",
                            address="http://123.56.169.183:8210",
                            debug_mode=1
                            )

    track_common = TrackCommon()
    track_common.udid = "abcd"
    track_common.user_id = "1234"
    track_common.distinct_id = "6039281029182710291"
    track_common.platform = Platform.IOS.value
    track_common.sdk_type = SdkType.IOS.value
    track_common.sdk_version = "1.0.1"
    track_common.screen_height = 650
    track_common.screen_width = 350
    track_common.manufacturer = "huawei"
    track_common.model = "huawei P40"
    track_common.network = Network.N_4G.value
    track_common.os = Os.IOS.value
    track_common.os_version = "12.1.1"
    track_common.carrier = Carrier.CHINA_UNICOM.value
    track_common.app_version = "1.0.1"

    appInstall = AppInstall()
    properties = [appInstall]

    track_info = TrackInfo()
    track_info.common = track_common
    track_info.properties = properties
    
    print(sync_client.track(track_info))
