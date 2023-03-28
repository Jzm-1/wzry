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
'cRand': '1679922686346',
'cSystem': 'android',
'cSystemVersionCode': '22',
'cSystemVersionName': '5.1.1',
'cpuHardware': 'qcom',
'encodeParam': 'im8lam6pXeV3MiAtfinif%2BX7cguDRL7BrG7E%2BinJOi84GowaRIYkMSE4ij%2BEymR68ISFAyca7a7lyC3IhTOc5pC5LRzFEXRWUS6Q1kgrr72dIebGIDp8XFHikXF%2FFHzlsG0oMw%3D%3D',
'gameAreaId': '1',
'gameId': '20001',
'gameOpenId': 'F26B8F1C87201FA1469671976D3FFD75',
'gameRoleId': '2092017349',
'gameServerId': '1301',
'gameUserSex': '2',
'openId': 'D621B704AE0CB7B838EF3206CF9A45BC',
'tinkerId': '2022674304_32_0',
'token': 'GfEBcVaN',
'userId': '1843580248',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '646',
'Host': 'ssl.kohsocialapp.qq.com:10001',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/4.9.1',
}
data = {'recommendPrivacy': '0',
'uniqueRoleId': '2092017349',
'cChannelId': '10003407',
'cClientVersionCode': '2022674304',
'cClientVersionName': '6.74.304',
'cCurrentGameId': '20001',
'cGameId': '20001',
'cGzip': '1',
'cRand': '1679929822407',
'cSystem': 'android',
'cSystemVersionCode': '22',
'cSystemVersionName': '5.1.1',
'cpuHardware': 'qcom',
'encodeParam': 'sLf5lPpALZtWKKgLuOkA+jjSK40QlHLPtIBPGs1jb79RLIrtq+1oJSGB6te6MDyxAkDeM1VejzSCTqiZ/lvQKErAnlrxW7EIaNADlpOG87bJrCZQziMKIg/mQvLCzXnI07CBKA==',
'gameAreaId': '1',
'gameId': '20001',
'gameOpenId': 'F26B8F1C87201FA1469671976D3FFD75',
'gameRoleId': '2092017349',
'gameServerId': '1301',
'gameUserSex': '2',
'openId': 'D621B704AE0CB7B838EF3206CF9A45BC',
'tinkerId': '2022674304_32_0',
'token': 'GfEBcVaN',
'userId': '1843580248',}
url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5getherolist'

resp = requests.post(url, headers=headers, data=data)
data = resp.json()

heroNum = data['data']["hasData"]["heroNum"]
skinNum = data['data']["hasData"]["skinNum"]
heroList = data['data']["heroList"]

for i in range(heroNum):
    print(heroList[i].get("name"))