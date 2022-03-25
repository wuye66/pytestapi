# -*- coding: UTF-8 -*-
import requests
import pytest
import json
import allure

@allure.story("登录")
@pytest.mark.one
def test_passport_login():
    host = 'https://passport.100tal.com'
    api = '/v1/web/login/pwd'
    url = host + api
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'client-id': '123601',
               'device-id': 'TAL1118EF6EBC6BDA1F6C942797A753FA4EB55E',
               'ver-num': '1.13.03'}

    data = 'symbol=13811385926&password=w12345678&source_type=2&domain=xueersi.com'

    r = requests.post(url=url, headers=headers, data=data)
    print(r.text)
    print(r.status_code)
