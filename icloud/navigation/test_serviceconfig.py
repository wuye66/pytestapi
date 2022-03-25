# -- coding: UTF-8 --
import json
import requests
import pytest
import allure

@allure.story("serviceconfig")
@pytest.mark.one
def test_icloud_navigation_serviceconfig(gettoken):

    host = 'https://classroom-api-online.speiyou.com'
    api = '/icloud/navigation/serviceconfig'

    #token = test_passport_login('13811385926','w12345678')
    headers = {'Connection': 'keep-alive', 'Content-Length': '504', 'stuId': '3807532', 'appClientType': 'xes',
               'Origin': 'owcr://classroom', 'lecturerId': '', 'stdSubject': '',
               'online_trace_id': 'pcStudent-e6834b6afaea204b26787987a85171f6', 'lang': 'ch',
               'systemDevice': 'Windows 10 Professional', 'deviceMemory': '8G', 'tutorId': '', 'liveType': '',
               'terminal': 'pc', 'Content-Type': 'application/json',
               'expireTime': '0', 'branchId': '',
               'token': gettoken,
               'version': '3.21.0.1680'}
    url = host + api
    data = {"app_cpu_rate": "10.157433", "app_mem_used": "376.644531",
                       "cpuType": "Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz", "cpu_rate": "8",
                       "disk_total": "447.000000", "disk_used": "78.000000", "dpi": 100, "gpu_total": "4095M, 4095M",
                       "gpu_type": "Intel(R) HD Graphics 5500, NVIDIA GeForce 840M", "gpu_used": "NA",
                       "gpus": [{"type": "Intel(R) HD Graphics 5500", "vram": 4095},
                                {"type": "NVIDIA GeForce 840M", "vram": 4095}], "mem_free": "1143.000000",
                       "mem_rate": "85", "mem_total": "8103.000000", "mem_used": "6960.000000",
                       "resolution": "1366x768"}
    r = requests.post(url=url, headers=headers, data=data)
    print(r.text)
    print(r.status_code)
