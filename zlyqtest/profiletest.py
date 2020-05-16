import sys
sys.path.append('..')

from zlyqsync.private_client import SyncClient
from zlyqmodel.profile import *

if __name__ == "__main__":
    syncClient = SyncClient(projectId=2,
                             apiKey="{your-api-key}",
                             address="{your-profile-node}"
                             )
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

    print(syncClient.setUserProfile(userProfile))

