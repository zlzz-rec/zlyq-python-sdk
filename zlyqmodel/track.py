from dataclasses import dataclass, asdict
from typing import List
from .common_define import Platform, Os, SdkType, Network, Carrier

import time
import datetime
import json

@dataclass
class TrackCommon():
    udid               : str = ""     
    user_id            : str = ""
    distinct_id        : int = 0
    app_id             : int = 0
    platform           : str = ""
    time               : datetime.datetime = "" 
    sdk_type           : str = ""
    sdk_version        : str = ""
    screen_height      : int = 0
    screen_width       : int = 0
    manufacturer       : str = ""
    model              : str = ""
    network            : str = ""
    os                 : str = ""
    os_version         : str = ""
    carrier            : str = ""
    app_version        : str = ""

    def __init__(self):
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@dataclass
class EventCommon():
    event         : str = ""
    event_time    : str = ""
    is_first_day  : int = 0
    is_first_time : int = 0
    is_login      : int = 0

@dataclass
class TrackInfo():
    project_id    : int = 0
    debug_mode    : int = 1
    type          : str = "track"
    common        : TrackCommon = None
    properties    : List[EventCommon] = None

@dataclass
class AppInstall(EventCommon):
    def __init__(self):
        self.event = "appInstall"
        self.event_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@dataclass
class AppStart(EventCommon):
    def __init__(self):
        self.event = "appStart"
        self.event_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@dataclass
class AppEnd(EventCommon):
    duration      : float = 0.0
    def __init__(self):
        self.event = "appEnd"
        self.event_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == "__main__":
    track_common = TrackCommon()
    track_common.udid = "abcd"
    track_common.user_id = "1234"
    track_common.distinct_id = "6039281029182710291"
    track_common.platform = Platform.IOS.value
    track_common.sdk_type = SdkType.IOS.value
    track_common.sdk_version = "1.0.1"
    track_common.screen_height = 650.0
    track_common.screen_width = 350.0
    track_common.manufacturer = "huawei"
    track_common.model = "huawei P40"
    track_common.network = Network.N_4G.value
    track_common.os = Os.IOS.value
    track_common.os_version = "12.1.1"
    track_common.carrier = Carrier.CHINA_UNICOM.value
    track_common.app_version = "1.0.1"

    app_install = AppInstall()
    properties = [app_install]
    
    track_info = TrackInfo()
    track_info.project_id = 2
    track_info.common = track_common
    track_info.properties = properties
    print(json.dumps(asdict(track_info)))



