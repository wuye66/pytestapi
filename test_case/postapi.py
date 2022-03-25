import requests
import json

class webrequest(object):
    def __init__(self):
        pass

    def Interface(self,host,api,data):
        url = host + api
        #print(url)
        a = {"invoke_info":{"pos_1":[{}],"pos_2":[{}],"pos_3":[{}]}}
        #data = json.loads(data)

        t = type(data)

        #data
        #data = str.encode(data)
        #c = json.loads(data)
        #print(type(r))
        #print(t)
        r = requests.post(url=url,json=data)
        #print(r.text)
        #print(r.status_code)
        return r.status_code

#a = webrequest()
#a.Interface('https://ug.baidu.com','/mcp/pc/pcsearch')