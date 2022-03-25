import requests
import json

class webrequest(object):
    def __init__(self):
        pass

    def Interface(self,host,api,data):
        url = host + api
        #print(url)
        #headers = {
#
        #}
        data = data
        requests.get
        r = requests.get(url=url,params=data)
        #print(r.text)
        #print(r.status_code)
        return r.status_code
