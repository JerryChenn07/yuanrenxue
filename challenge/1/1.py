import base64
import hashlib
import time

import requests

count = 0
for i in range(1, 85):
    a = '9622'
    timestamp = str(int(time.time()))
    # timestamp = str(1617264163)
    to_base64 = base64.b64encode(f"{a + timestamp}".encode('utf-8'))
    tokens = hashlib.md5(to_base64).hexdigest()
    print(tokens)

    headers = {
        'Proxy-Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'timestamp': timestamp,
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'safe': tokens,
        'Referer': 'http://www.python-spider.com/challenge/1',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    }

    params = {'page': str(i), 'count': '14'}

    response = requests.get('http://www.python-spider.com/challenge/api/json', headers=headers, params=params)
    json_text = response.json()
    infos = json_text.get('infos')
    for j in infos:
        if '招' in j['message']:
            count += 1

print(count)
