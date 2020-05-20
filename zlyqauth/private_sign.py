import time
import hashlib

def addSign(params, apiKey):
    params['time'] = int(time.time() * 1000)

    keys = [key for key in params.keys()]
    keys.sort()

    values = []
    for key in keys:
        values.append(key + '=' + str(params[key]))

    string = "&".join(values)

    salt = apiKey
    signature = hashlib.md5((salt + "&" + string).encode(encoding='UTF-8')).hexdigest()

    return signature, string
