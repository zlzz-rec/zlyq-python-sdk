from dataclasses import dataclass, asdict
from typing import List
from enum import Enum
from .common import *

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
    common:TrackCommon = None
    properties:List[EventCommon] = None

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
    trackCommon = TrackCommon()
    trackCommon.udid = "abcd"
    trackCommon.user_id = "1234"
    trackCommon.distinct_id = "6039281029182710291"
    trackCommon.platform = Platform.IOS.value
    trackCommon.sdk_type = SdkType.IOS.value
    trackCommon.sdk_version = "1.0.1"
    trackCommon.screen_height = 650.0
    trackCommon.screen_width = 350.0
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
    print(json.dumps(asdict(trackInfo)))



