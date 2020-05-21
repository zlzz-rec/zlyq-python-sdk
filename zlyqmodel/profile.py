from dataclasses import dataclass, asdict
from typing import List
from .common_define import DebugMode, Os, SdkType

import datetime
import time
import json

@dataclass
class UserProfileCommon():
    distinct_id         : str = ""
    user_id             : str = ""
    time                : datetime.datetime = ""
    type                : str = ""

    def __init__(self):
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@dataclass
class UserProfile():
    user_id             : str = ""	
    distinct_id	        : str = ""
    udid	        : str = ""
    birthday	        : str = ""
    name                : str = ""
    gender	        : str = ""
    browser	        : str = ""
    browser_version     : str = ""
    first_visit_time    : str = ""
    utm_source	        : str = ""
    utm_media	        : str = ""
    utm_campaign        : str = ""
    utm_content	        : str = ""
    utm_term	        : str = ""
    os	                : str = ""
    os_version	        : str = ""
    sdk_type	        : str = ""
    sdk_version	        : str = ""
    app_version	        : str = ""
    update_time	        : datetime.datetime = ""

    def __init__(self):
        self.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@dataclass
class UserProfileInfo():
    project_id          : int = 0
    debug_mode          : str = DebugMode.NO_DEBUG_MODE.value
    type                : str = "user_profile"
    common              : UserProfileCommon = None
    property            : UserProfile = None

if __name__ == "__main__":
    user_profile = UserProfile()
    user_profile.user_id = "123"
    user_profile.distinct_id = "6020103928102918274"
    user_profile.udid = "abcdefg"
    user_profile.birthday = "1990-01-01 20:00:00"
    user_profile.name = "小脑斧"
    user_profile.gender = "男"
    user_profile.browser = "chrome"
    user_profile.browser_version = "1.0.0"
    user_profile.first_visit_time = "2020-02-02 20:00:00"
    user_profile.utm_source = "toutiao"
    user_profile.utm_media = "cpc"
    user_profile.utm_campaign = "app"
    user_profile.utm_content = "20200101"
    user_profile.utm_term = "delicacy"
    user_profile.os = Os.IOS.value
    user_profile.os_version = "10.0.1"
    user_profile.sdk_type = SdkType.IOS.value
    user_profile.sdk_version = "1.0.1"
    user_profile.app_version = "2.0.0"

    user_profile_common = UserProfileCommon()
    user_profile_common.distinct_id = "6039281029182710291"
    user_profile_common.user_id = "1234"
    user_profile_common.type = "1234"

    user_profile_info = UserProfileInfo()
    user_profile_info.common = user_profile_common 
    user_profile_info.property = user_profile

    print(json.dumps(asdict(user_profile_info)))
