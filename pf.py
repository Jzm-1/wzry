import requests
import time
import pathlib
from lxml import etree

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
url = "https://pvp.qq.com/web201605/js/herolist.json"
resp = requests.get(url, headers=headers)
all_content = resp.json()
url1 = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/"
url2 = "https://pvp.qq.com/web201605/herodetail/"
url3 = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"

for each in all_content:
    cname = each.get("cname")
    ename = str(each.get("ename"))
    pathlib.Path(f'/data/wzry/王者荣耀皮肤/{cname}').mkdir()

for each in all_content:
    cname = each.get("cname")
    ename = str(each.get("ename"))
    try:
        resp = requests.get(f"{url1}{ename}/{ename}.jpg", headers=headers)
    except:
        print("未知异常")
        continue
    with open(f"王者荣耀皮肤/{cname}/{cname}.jpg", "wb") as f:
        f.write(resp.content)
    print(f"正在保存{cname}")
    time.sleep(1)

for each in all_content:
    cname = each.get("cname")
    ename = str(each.get("ename"))
    try:
        resp = requests.get(f"{url2}{ename}.shtml")
    except:
        print("未知异常")
        continue
    resp.encoding = "gbk"
    e = etree.HTML(resp.text)
    pf = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')
    pf = pf[0].split("|")
    time.sleep(1)

    for i,each in enumerate(pf):
        if "&" in each:
            t = each.index("&")
            pf_name = each[0:t]
        else:
            pf_name = each
        resp = requests.get(f"{url3}{ename}/{ename}-bigskin-{i+1}.jpg", headers=headers)
        with open(f"王者荣耀皮肤/{cname}/{pf_name}.jpg", "wb") as f:
            f.write(resp.content)
        print(f"正在保存{pf_name}")
        time.sleep(1)


