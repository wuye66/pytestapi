# -*- coding: UTF-8 -*-

import pytest
import requests
import json

user = '13811385926'
password = 'w12345678'


@pytest.fixture(scope="session", autouse=True)
def gettoken():
    host = 'https://passport.100tal.com'
    api = '/v1/web/login/pwd'
    url = host + api
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'client-id': '123601',
               'device-id': 'TAL1118EF6EBC6BDA1F6C942797A753FA4EB55E',
               'ver-num': '1.13.03'}

    data = 'symbol=' + user + '&password=' + password + '&source_type=2&domain=xueersi.com'

    r = requests.post(url=url, headers=headers, data=data)
    token = json.loads(r.text).get('data').get('passport_token')
    print('获取token完成')
    return token
    # flag = 1
    # yield flag
