import requests
from requests import Session


class Api_common:
    def __init__(self):
        self.session = Session()
        self.base_url="http://localhost"
        self.headers={
            "Content-Type": "application/json"
        }
    def request(self,path,**kwargs):
        url=path if path.startswith("http") else r"{self.base_url}/{path.lstrip('/')}"
    def feihua(self):
        print("feihua")
    #提供鉴权头
    def set_token(self,token):
        self.headers["Authorization"] =f"Bearer {token}"
    #post的请求方法
    def send_post(self,url=None,Json_date=None,headers=None):
        full_url=self.base_url+url
        res=self.session.post(full_url,json=Json_date,headers=self.headers)
        return res
    #Get的请求方法
    def send_get(self,url=None,params=None,headers=None):
        headers=self.headers
        full_url=self.base_url+url
        res=self.session.get(full_url,params=params,headers=headers)
        return res