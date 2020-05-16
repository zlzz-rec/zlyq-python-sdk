import time
import hashlib

def addSign(urlParams, apiKey):
    urlParams['time'] = int(time.time() * 1000)

    keys = [key for key in urlParams.keys()]
    keys.sort()

    values = []
    for key in keys:
        values.append(key + '=' + str(urlParams[key]))

    string = "&".join(values)

    salt = apiKey
    signature = hashlib.md5((salt + "&" + string).encode(encoding='UTF-8')).hexdigest()

    return signature, string
