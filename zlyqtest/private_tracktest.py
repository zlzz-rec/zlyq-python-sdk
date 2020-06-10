from ..zlyqsync.private_client import SyncClient
from ..zlyqmodel.private_track import TrackCommon, EventCommon, TrackInfo, AppInstall
from ..zlyqmodel.common_define import Platform, SdkType, Network, Os, Carrier, DebugMode
from dataclasses import dataclass
import time

@dataclass
class ItemEnd(EventCommon):
    item_id: str = ""
    channel_id: int = 0
    producer_id: int = 0
    duration: int = 0

    def __init__(self):
        self.event = "item_end"
        self.event_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def presetEvent():
    # 客户端透传common参数
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

    # 引入预置事件
    appInstall = AppInstall()
    properties = [appInstall]

    track_info = TrackInfo()
    track_info.common = track_common
    track_info.properties = properties
    return track_info

def customEvent():
    # 客户端透传common参数
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

    # 需要自定义一个继承EventCommon的结构
    item_end = ItemEnd()
    item_end.item_id = "1020912830918290"
    item_end.channel_id = "4"
    item_end.producer_id = "192839128391928391"
    item_end.duration = 12391

    properties = [item_end]
    track_info = TrackInfo()
    track_info.common = track_common
    track_info.properties = properties
    return track_info

if __name__ == "__main__":
    sync_client = SyncClient(project_id=1,
                            #api_key="{your-api-key}",
                            #address="{your-address}",
                            api_key="abcdefg",
                            address="http://47.93.23.69:8210",
                            debug_mode=DebugMode.DEBUG_AND_IMPORT.value
                            )
    
    # 预置事件埋点
    preset_track_info = presetEvent()
    print(sync_client.track(preset_track_info))

    # 自定义事件埋点
    custom_track_info = customEvent()
    print(sync_client.track(custom_track_info))
