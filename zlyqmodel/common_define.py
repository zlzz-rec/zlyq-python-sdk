from enum import Enum

class Platform(Enum):
    IOS = "Ios"
    ANDROID = "Android"
    H5 = "H5"
    MP = "Mp"

class SdkType(Enum):
    IOS = "Ios"
    ANDROID = "Android"
    H5 = "H5"
    MP = "Mp"

class Network(Enum):
    N_3G = "3G"
    N_4G = "4G"
    N_5G = "5G"
    N_WIFI = "wifi"

class Os(Enum):
    IOS = "Ios"
    ANDROID = "Android"
    WINDOWS_PHONE = "Windows phone"
    YUN_OS = "YunOS"
    SYMBIAN = "Symbian"

class Carrier(Enum):
    CHINE_TELECOM = "中国电信"
    CHINA_MOBILE = "中国移动"
    CHINA_UNICOM = "中国联通"


if __name__ == "__main__":
    pass
