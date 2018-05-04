# -*- coding: utf-8 -*-

import requests

def subscribe(item_id):
    url = 'https://hz.fang.anjuke.com/aifang/web/loupan/ajax/subscribebind/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }
    cookies = {
        # 'aQQ_ajkguid': '3A24443D-4861-94BC-171E-SX0504143055',
        # 'sessid': 'F2A8680A-F863-143D-D0AE-SX0504143055',
        # 'ajk_member_id': '29013218',
        # 'ajk_member_key': '7f6b7c1fcf4e7dc8ca2f12f81ee5f8ff',
        'aQQ_ajkauthinfos': 'vcQd5xuPg4QLOKU5BC%2BRWmgYIFXbDDjsWweHhOIuijTMnohIp2y0kpupFKV59gYDP%2FNrawLYrv%2Fjnu1ssDYXZe475TMmV0WkX8LO',
    }

    payload = {
        'subscribe_type': 'subscribe',
        'source_id': item_id,
        'sub_from': 101,
        'category': 3,
        'check': 0
    }

    r = requests.post(url, data=payload, headers=headers, cookies=cookies, verify=False)
    if r.status_code == requests.codes.ok:
        data = r.json()
        status = data['status']
        if status == 0:
            return True
        else:
            print(data)
            print(data['msg'])
            return False
    else:
        print('error', r.content())
        return False

if __name__ == '__main__':
    subscribe(430990)


