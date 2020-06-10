from enum import Enum

class Platform(Enum):
    IOS = "iOS"
    ANDROID = "Android"
    H5 = "H5"
    MP = "Mp"

class SdkType(Enum):
    IOS = "iOS"
    ANDROID = "Android"
    H5 = "H5"
    MP = "Mp"

class Network(Enum):
    N_3G = "3G"
    N_4G = "4G"
    N_5G = "5G"
    N_WIFI = "wifi"

class Os(Enum):
    IOS = "iOS"
    ANDROID = "Android"
    WINDOWS_PHONE = "Windows phone"
    YUN_OS = "YunOS"
    SYMBIAN = "Symbian"

class Carrier(Enum):
    CHINE_TELECOM = "中国电信"
    CHINA_MOBILE = "中国移动"
    CHINA_UNICOM = "中国联通"

class DebugMode(Enum):
    NO_DEBUG_MODE = "no_debug"
    DEBUG_AND_IMPORT = "debug_and_import"
    DEBUG_AND_NOT_IMPORT = "debug_and_not_import"


if __name__ == "__main__":
    pass
