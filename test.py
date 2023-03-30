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
'cRand': '1680147203685',
'cSystem': 'android',
'cSystemVersionCode': '22',
'cSystemVersionName': '5.1.1',
'cpuHardware': 'qcom',
'encodeParam': 'lWRl8ORglqoOin%2FAV5za0MDwUxi8JlqHSSNVpgsRVIdTU09S5xNDacPt0wGAJGz0nScdZW1bJRVm19E98zaJKrVs2kS7lu7sTl7rMjvonhjvVGi0CqSXUME%2B%2F7rMMphT5kvc4g%3D%3D',
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
'Content-Length': '640',
'Host': 'ssl.kohsocialapp.qq.com:10001',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/4.9.1',
}
data = {'recommendPrivacy': '0',
'uniqueRoleId': '107113694',
'cChannelId': '10003407',
'cClientVersionCode': '2022674304',
'cClientVersionName': '6.74.304',
'cCurrentGameId': '20001',
'cGameId': '20001',
'cGzip': '1',
'cRand': '1680147203685',
'cSystem': 'android',
'cSystemVersionCode': '22',
'cSystemVersionName': '5.1.1',
'cpuHardware': 'qcom',
'encodeParam': 'lWRl8ORglqoOin/AV5za0MDwUxi8JlqHSSNVpgsRVIdTU09S5xNDacPt0wGAJGz0nScdZW1bJRVm19E98zaJKrVs2kS7lu7sTl7rMjvonhjvVGi0CqSXUME+/7rMMphT5kvc4g==',
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
url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5getherolist'

resp = requests.post(url, headers=headers, data=data)
data = resp.json()

heroNum = data['data']["hasData"]["heroNum"]
skinNum = data['data']["hasData"]["skinNum"]
heroList = data['data']["heroList"]

print(heroNum, skinNum)

for i in range(heroNum):
    print(heroList[i].get("name"))