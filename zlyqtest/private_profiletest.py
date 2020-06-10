from ..zlyqsync.private_client import SyncClient
from ..zlyqmodel.private_profile import UserProfile, UserProfileCommon, UserProfileInfo, DebugMode

if __name__ == "__main__":
    sync_client = SyncClient(project_id=1,
                            #api_key="{your-api-key}",
                            #address="{your-address}",
                            api_key="abcdefg",
                            address="http://47.93.23.69:8210",
                            debug_mode=DebugMode.DEBUG_AND_IMPORT.value
                            )

    user_profile = UserProfile()
    user_profile.birthday = "1990-01-01 20:00:00"
    user_profile.name = "小脑斧"
    user_profile.gender = "男"
    user_profile.utm_source = "toutiao"
    user_profile.utm_media = "cpc"
    user_profile.utm_campaign = "app"
    user_profile.utm_content = "20200101"
    user_profile.utm_term = "delicacy"

    user_profile_common = UserProfileCommon()
    user_profile_common.distinct_id = "6039819281729382719"
    user_profile_common.user_id = "1234"

    user_profile_info = UserProfileInfo()
    user_profile_info.common = user_profile_common
    user_profile_info.property = user_profile

    print(user_profile_info)
    #print(sync_client.setUserProfileOnce(user_profile_info))
    print(sync_client.setUserProfile(user_profile_info))
