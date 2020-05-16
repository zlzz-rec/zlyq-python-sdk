from dataclasses import dataclass, asdict
from typing import List
from .common import *

import datetime
import time
import json

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
    is_deleted	        : int = 0
    update_time	        : datetime.datetime = ""

    def __init__(self):
        self.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == "__main__":
    userProfile = UserProfile()

    userProfile.user_id = "123"
    userProfile.distinct_id = "6020103928102918274"
    userProfile.udid = "abcdefg"
    userProfile.birthday = "1990-01-01 20:00:00"
    userProfile.name = "小脑斧"
    userProfile.gender = "男"
    userProfile.browser = "chrome"
    userProfile.browser_version = "1.0.0"
    userProfile.first_visit_time = "2020-02-02 20:00:00"
    userProfile.utm_source = "toutiao"
    userProfile.utm_media = "cpc"
    userProfile.utm_campaign = "app"
    userProfile.utm_content = "20200101"
    userProfile.utm_term = "delicacy"
    userProfile.os = Os.IOS.value
    userProfile.os_version = "10.0.1"
    userProfile.sdk_type = SdkType.IOS.value
    userProfile.sdk_version = "1.0.1"
    userProfile.app_version = "2.0.0"

    print(asdict(userProfile))
