import requests

headers = {'Content-Encrypt': '',
'Accept-Encrypt': '',
'NOENCRYPT': '1',
'X-Client-Proto': 'https',
'cChannelId': '10003407',
'cClientVersionCode': '2022674304',
'cClientVersionName': '6.74.304',
'cCurrentGameId': '20001',
'cGameId': '20001',
'cGzip': '1',
'cRand': '1680148143124',
'cSystem': 'android',
'cSystemVersionCode': '22',
'cSystemVersionName': '5.1.1',
'cpuHardware': 'qcom',
'encodeParam': 'aOjTTlVQOpkThjC7Qx1%2BAo6c%2B4LFl2Zf9lDFtUWUp%2BHs%2BurWEo4potGDCG02Ja4KVn7%2FKsIrvmyBv%2BRafGXApvAXgntw%2F4vJYowodmRIPlnPOJCMiEshSCOZ4cdVjFwdz2Mv%2BQ%3D%3D',
'gameAreaId': '1',
'gameId': '20001',
'gameOpenId': '833CA31ED9E126C28212F8DBB3681361',
'gameRoleId': '107113694',
'gameServerId': '1127',
'gameUserSex': '1',
'openId': '4E12F6D761B18B43B5091B13B3510D00',
'tinkerId': '2022674304_32_0',
'token': '9Nh3sftC',
'userId': '92496228',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '654',
'Host': 'ssl.kohsocialapp.qq.com:10001',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/4.9.1',
}
data = {'noCache': '0',
'roleId': '107113694',
'recommendPrivacy': '0',
'cChannelId': '10003407',
'cClientVersionCode': '2022674304',
'cClientVersionName': '6.74.304',
'cCurrentGameId': '20001',
'cGameId': '20001',
'cGzip': '1',
'cRand': '1680148143124',
'cSystem': 'android',
'cSystemVersionCode': '22',
'cSystemVersionName': '5.1.1',
'cpuHardware': 'qcom',
'encodeParam': 'aOjTTlVQOpkThjC7Qx1+Ao6c+4LFl2Zf9lDFtUWUp+Hs+urWEo4potGDCG02Ja4KVn7/KsIrvmyBv+RafGXApvAXgntw/4vJYowodmRIPlnPOJCMiEshSCOZ4cdVjFwdz2Mv+Q==',
'gameAreaId': '1',
'gameId': '20001',
'gameOpenId': '833CA31ED9E126C28212F8DBB3681361',
'gameRoleId': '107113694',
'gameServerId': '1127',
'gameUserSex': '1',
'openId': '4E12F6D761B18B43B5091B13B3510D00',
'tinkerId': '2022674304_32_0',
'token': '9Nh3sftC',
'userId': '92496228',}
url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5getheroskinlist'

resp = requests.post(url, headers=headers, data=data)

data = resp.json()['data']["heroSkinList"]

num = 0
for each in data:
    if each.get("iBuy") != None:
        print(each.get("szTitle"))
        num += 1
print(num)